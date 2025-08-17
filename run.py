import logging as log
import argparse
import time
import sys

from config import SUPPORTED_GAMES
from scraper import get_all_servers, players_from_servers, update_dataset

log.basicConfig(level=log.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

def _run_cycle(output_file: str, game: str, batch_size: int):
    data = get_all_servers(game)
    if not data:
        return False
    player_names = players_from_servers(data)
    log.info(f"Updating player stats dataset: {output_file}")
    update_dataset(game = game, dataset_path = output_file, names = player_names, batch_size = batch_size)
    return True

def _run_from_file(output_file: str, input_file: str, game: str, batch_size: int):
    player_names = []
    with open(input_file, 'r') as f:
        for name in f:
            player_names.append(name.strip())
    log.info(f"Loaded {len(player_names)} player names from {input_file}")
    log.info(f"Updating player stats dataset: {output_file}")
    update_dataset(game = game, dataset_path = output_file, names = player_names, batch_size = batch_size)

def main():
    parser = argparse.ArgumentParser(description="Battlefield 4 Player Stats Scraper")
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=str,
        help="Path to the output CSV file for player statistics.",
    )
    parser.add_argument(
        "-g",
        "--game",
        required=True,
        type=str,
        choices=SUPPORTED_GAMES,
        help=f"Game to scrape data from. Supported: {SUPPORTED_GAMES}",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default=None,
        help="Path to a text file containing one player name per line.",
    )
    parser.add_argument(
        "-d",
        "--delay",
        type=int,
        default=0,
        help="Delay in seconds between scraping cycles. (default: 0s)",
    )
    parser.add_argument(
        "-b",
        "--batch",
        type=int,
        default=1,
        help="Number of players per batch to write to the dataset. (default: 1)",
    )
    parser.add_argument(
        "-inf",
        "--infinite",
        action="store_true",
        help="Run scraper in endless mode.",
    )   
    args = parser.parse_args()
    
    if args.input:
        _run_from_file(args.output, args.input, args.game, args.batch)
        log.info("Scraping process completed. Exiting.")
        sys.exit(0)
        
    cycle = 0
    while args.infinite or cycle == 0:
        cycle+=1
        try:
            log.info(f"Scraping cycle {cycle} started.")
            success = _run_cycle(args.output, args.game, args.batch)
            
            if success:
                log.info(f"Scraping cycle {cycle} completed.")
            else:
                log.error(f"Scraping cycle {cycle} failed.")
                
            if args.infinite:
                log.info(f"Waiting {args.delay}s for next cycle...")
                time.sleep(args.delay)
            else:
                log.info("Scraping process completed. Exiting.")
                break
                
        except KeyboardInterrupt:
            log.info("Interrupted by user. Shutting down.")
            sys.exit(0)
        except Exception as e:
            log.exception(e)


if __name__ == "__main__":
    main()