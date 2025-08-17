# battlefield-stats-scraper
A comprehensive data collection tool that builds rich datasets of Battlefield player statistics using publicly available APIs. The scraper automatically gathers data from active servers, processes it, and stores it in a structured CSV format for data analysis. 

## Features
* **Automated Data Scraper:** Continuously fetches data from all active Battlefield servers.
* **Comprehensive Stat Collection:** Gathers a wide range of player stats, from general performance metrics like K/D to detailed stats for weapons and vehicles
* **Well Organized Updates:** Efficiently adds new, unique players to the dataset without creating duplicates

## Supported Games
Currently, the scraper supports:
* **Battlefield 3:** use `-g bf3` in command line arguments
* **Battlefield 4:** use `-g bf4` in command line arguments

**Planned Support:** The project uses an extensible architecture designed to easily add support for other Battlefield titles.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/chastertlye/battlefield-stats-scraper.git
   cd battlefield-stats-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
The data scraper is run from the command line using `run.py`. Customize its behavior with the following arguments:

### Required Arguments
* `-o, --output`: Path to the output CSV file for player statistics
* `-g, --game`: Game to scrape data from (see supported games list)

### Optional Arguments
* `-i, --input`: Path to a text file containing one player name per line. If provided, the scraper will only fetch stats for players listed in this file.
* `-d, --delay`: Delay in seconds between scraping cycles (default: 0)
* `-b, --batch`: Number of players per batch to write to the dataset (default: 1)
* `-inf, --infinite`: Run scraper in continious mode. You can stop it with `Ctrl+C`

### Usage Example
**Basic single-run scraping:**
```bash
python run.py -o dataset.csv -g bf4
```
**Continuous scraping with 60-second intervals:**
```bash
python run.py -o dataset.csv -g bf4 -d 60 -inf
```
**Scrape specific players from file:**
```bash
python run.py -o dataset.csv -g bf4 -i player_list.txt
```

## Data Collected
The scraper gathers a wide array of statistics, stored in a single row per player in the final dataset. This includes:

* **General Performance Metrics:** K/D ratio, accuracy, score per minute, etc
* **Weapon Statistics:** Performance with different weapons
* **Vehicle Statistics:** Performance with different vehicles
* **Game Mode Performance:** Statistics across different game modes
* **Progressive Stats:** Rank and unlock progress