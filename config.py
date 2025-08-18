# Base URLs for the APIs used
BFLIST_BASE = "https://api.bflist.io/v2/"
GAMETOOLS_BASE = "https://api.gametools.network/"

SUPPORTED_GAMES = ['bf3', 'bf4', 'bfh']

BF3_PLAYER_BASE_STATS = [
    "userName",
    "id",
    "rank",
    "scorePerMinute",
    "killsPerMinute",
    "winPercent",
    "killDeath",
    "quits",
    "accuracy",
    "secondsPlayed",
    "kills",
    "deaths",
    "wins",
    "loses",
    "avengerKills",
    "saviorKills",
    "heals",
    "revives",
    "repairs",
    "resupplies",
    "killAssists",
    "skill",
    "longestHeadShot",
    "highestKillStreak",
]

BF3_PLAYER_ADDITIONAL_STATS = [
    ["classes", "className", "score"]
]

BF4_PLAYER_BASE_STATS = [
    "userName",
    "id",
    "rank",
    "scorePerMinute",
    "killsPerMinute",
    "winPercent",
    "killDeath",
    "quits",
    "accuracy",
    "headshots",
    "secondsPlayed",
    "kills",
    "deaths",
    "wins",
    "loses",
    "avengerKills",
    "saviorKills",
    "headShots",
    "heals",
    "revives",
    "repairs",
    "resupplies",
    "killAssists",
    "skill",
    "longestHeadShot",
    "highestKillStreak",
]

BF4_PLAYER_ADDITIONAL_STATS = [
    ["classes", "className", "score"],
    ["gamemodes", "gamemodeName", "score"],
    ["progress", "progressName", "current"],
]

BFH_PLAYER_BASE_STATS = [
  "userName",
  "id",
  "rank",
  "scorePerMinute",
  "killsPerMinute",
  "winPercent",
  "killDeath",
  "accuracy",
  "secondsPlayed",
  "kills",
  "deaths",
  "wins",
  "loses",
  "killAssists",
  "enforcer",
  "mechanic",
  "operator",
  "professional",
  "hacker",
  "cashPerMinute"
]

BFH_PLAYER_ADDITIONAL_STATS = [
    ["progress", "progressName", "current"],
]

STATS_MANAGER = {
    "bf3":{
        "PLAYER_BASE_STATS": BF3_PLAYER_BASE_STATS,
        "PLAYER_ADDITIONAL_STATS": BF3_PLAYER_ADDITIONAL_STATS,
    },
    "bf4":{
        "PLAYER_BASE_STATS": BF4_PLAYER_BASE_STATS,
        "PLAYER_ADDITIONAL_STATS": BF4_PLAYER_ADDITIONAL_STATS,
    },
    "bfh":{
        "PLAYER_BASE_STATS": BFH_PLAYER_BASE_STATS,
        "PLAYER_ADDITIONAL_STATS": BFH_PLAYER_ADDITIONAL_STATS,
    }
}