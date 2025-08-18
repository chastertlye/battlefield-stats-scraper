# Base URLs for the APIs used
BFLIST_BASE = "https://api.bflist.io/v2/"
GAMETOOLS_BASE = "https://api.gametools.network/"

AUTO_SCRAPING_SUPPORTED_GAMES = ['bf3', 'bf4', 'bfh'] # Games that support auto scraping from servers
ALL_SUPPORTED_GAMES = ['bf3', 'bf4', 'bfh', 'bf1', 'bfv'] # All games supported by the scraper

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

BF1_PLAYER_BASE_STATS = [
    "userName",
    "id",
    "rank",
    "skill",
    "scorePerMinute",
    "killsPerMinute",
    "winPercent",
    "accuracy",
    "headshots",
    "secondsPlayed",
    "killDeath",
    "infantryKillDeath",
    "infantryKillsPerMinute",
    "kills",
    "deaths",
    "wins",
    "loses",
    "longestHeadShot",
    "revives",
    "dogtagsTaken",
    "highestKillStreak",
    "roundsPlayed",
    "awardScore",
    "bonusScore",
    "squadScore",
    "avengerKills",
    "saviorKills",
    "headShots",
    "heals",
    "repairs",
    "killAssists",
]

BF1_PLAYER_ADDITIONAL_STATS = [
    ["classes", "className", "score"],
    ["gamemodes", "gamemodeName", "score"],
    ["progress", "progressName", "current"],
]

BFV_PLAYER_BASE_STATS = [
    "userName",
    "id",
    "rank",
    "skill",
    "scorePerMinute",
    "killsPerMinute",
    "winPercent",
    "accuracy",
    "headshots",
    "secondsPlayed",
    "killDeath",
    "infantryKillDeath",
    "infantryKillsPerMinute",
    "kills",
    "deaths",
    "wins",
    "loses",
    "longestHeadShot",
    "revives",
    "dogtagsTaken",
    "highestKillStreak",
    "roundsPlayed",
    "awardScore",
    "bonusScore",
    "squadScore",
    "currentRankProgress",
    "totalRankProgress",
    "avengerKills",
    "saviorKills",
    "headShots",
    "heals",
    "repairs",
    "killAssists",
]

BFV_PLAYER_ADDITIONAL_STATS = []

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
    },
    "bf1":{
        "PLAYER_BASE_STATS": BF1_PLAYER_BASE_STATS,
        "PLAYER_ADDITIONAL_STATS": BF1_PLAYER_ADDITIONAL_STATS,
    },
    "bfv":{
        "PLAYER_BASE_STATS": BFV_PLAYER_BASE_STATS,
        "PLAYER_ADDITIONAL_STATS": BFV_PLAYER_ADDITIONAL_STATS,
    }
}