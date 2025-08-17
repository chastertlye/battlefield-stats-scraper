import logging as log
import os

import pandas as pd
import requests
from tqdm import tqdm

from config import (
    BFLIST_BASE,
    GAMETOOLS_BASE,
    STATS_MANAGER
)

log.basicConfig(level=log.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")


def get_livestats(game):
    """Fetches live statistics about the number of active servers and players currently online for Battlefield"""

    response = requests.get(f"{BFLIST_BASE}{game}/livestats").json()
    log.info(
        f'Succesfully fetched livestats: {response["servers"]} servers and {response["players"]} players active'
    )
    return response["servers"], response["players"]


def get_all_servers(game):
    """Retrieves data for all currently active Battlefield servers"""

    total_servers, _ = get_livestats(game)
    data = {"servers": []}
    
    # Variables for cursor-based pagination
    hasMore = True
    cursor = None
    after = None

    try:
        with tqdm(total=total_servers, desc="Fetching servers") as pbar:
            while hasMore:
                payload = {}
                if cursor and after:
                    payload = {"cursor": cursor, "after": after}
                response = requests.get(f"{BFLIST_BASE}{game}/servers", params=payload).json()

                cursor = response["cursor"]
                hasMore = response["hasMore"]
                last_ip, last_port = (
                    response["servers"][-1]["ip"],
                    response["servers"][-1]["port"],
                )
                after = f"{last_ip}:{last_port}"             
                pbar.update(len(response["servers"]))
                
                # Filters for servers that have at least one player.
                active_servers = [
                    s for s in response["servers"] if len(s["players"]) > 0
                ]
                data["servers"].extend(active_servers)

        log.info(f"Found {len(data['servers'])} populated servers.")
        return data

    except Exception:
        log.error("Error fetching servers", exc_info=True)
        return None


def players_from_servers(data: dict):
    """Extracts player names from a list of servers"""

    players = []
    for server in data["servers"]:
        for player in server["players"]:
            name = player["name"]
            players.append(name)
    players = set(players)
    log.info(f"Found {len(players)} players currently online.")
    return players


def flatten_map(d: dict, sep: str = "-"):
    """Flatten double-level dict into single-level dict"""

    d_flat = {
        f"{type_key}{sep}{k}": v
        for type_key, type_dict in d.items()
        for k, v in type_dict.items()
    }
    return d_flat


def get_player_stats(name: str, game: str):
    """Retrieves detailed stats for a given player by name"""
    GAME_STATS = STATS_MANAGER[game]
    try:
        response = requests.get(
            f"{GAMETOOLS_BASE}{game}/all", params={"name": name, "format_values": False}
        ).json()
        # Extracts base player stats
        player_stats = {k: response[k] for k in GAME_STATS["PLAYER_BASE_STATS"]}

        # Aggregates weapon stats
        weapon_stats = {}
        for w in response["weapons"]:
            weapon_stats[w["weaponName"]] = {
                "kills": w["kills"],
                "kpm": w["killsPerMinute"],
                "accuracy": w["accuracy"],
                "hskr": w["headshots"],
            }
            
        # Specific weapon settings for each game
        if game == 'bf4':
            # Phantom bow doesn't show if player didn't use it once, so we need to add it manually
            if not "phantom" in weapon_stats:
                weapon_stats["phantom"] = {
                    "kills": 0,
                    "kpm": 0.0,
                    "accuracy": 0.0,
                    "hskr": 0.0,
                }
        weapons_flat = flatten_map(weapon_stats)
        player_stats.update(weapons_flat)

        # Aggregates vehicle stats
        vehicle_stats = {}
        for v in response["vehicles"]:
            vehicle_stats[v["vehicleName"]] = {
                "kills": v["kills"],
                "kpm": v["killsPerMinute"],
                "destroyed": v["destroyed"],
                "time_in": v["timeIn"],
            }
        vehicles_flat = flatten_map(vehicle_stats)
        player_stats.update(vehicles_flat)

        # Aggregates additional stats
        additional_stats = {}
        for stat_category, name_key, value_key in GAME_STATS["PLAYER_ADDITIONAL_STATS"]:
            for item in response[stat_category]:
                additional_stats[item[name_key]] = {
                    value_key: item[value_key]
                }
        additional_flat = flatten_map(additional_stats)
        player_stats.update(additional_flat)
        return player_stats

    except Exception:
        return None


def update_dataset(game : str, dataset_path: str, names: list, batch_size: int):
    """Updates a CSV dataset with new player stats."""

    exists = os.path.isfile(dataset_path)
    existing_names = set()
    existing_ids = set()
    if exists:
        stats_df = pd.read_csv(dataset_path, usecols=["userName", "id"])
        existing_names = set(stats_df["userName"].values)
        existing_ids = set(stats_df["id"].values)
        log.info(f"Loaded {len(existing_names)} existing players from {dataset_path}.")

    new_names_count = 0
    new_names = [n for n in names if not n in existing_names]

    batch = []
    for name in tqdm(new_names, desc="Fetching players' stats"):
        for _ in range(3):
            stats = get_player_stats(name, game)
            if stats:
                break

        if stats:
            if not stats["id"] in existing_ids:
                batch.append(stats)

                # Write batch
                if len(batch) >= batch_size:
                    new_players_df = pd.DataFrame(batch)
                    new_players_df.to_csv(
                        dataset_path, mode="a", index=False, header=not exists
                    )
                    batch = []
                    exists = True
                    new_names_count += batch_size

    # Write any remaining players in the last batch
    if batch:
        new_players_df = pd.DataFrame(batch)
        new_players_df.to_csv(dataset_path, mode="a", index=False, header=not exists)
        new_names_count += len(batch)

    if new_names_count:
        log.info(f"Added {new_names_count} new players to the dataset")
    else:
        log.warning("No new players were added to dataset")
