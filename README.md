# battlefield-stats-scraper
This project's main goal is to build a rich dataset of Battlefield player statistics. It uses publicly available APIs to gather data from active servers, process it, and store it in a structured format. The collected data is intended for data analysis. 

## Features
* **Automated Data Scraper:** Continuously fetches data from all active Battlefield servers.
* **Comprehensive Stat Collection:** Gathers a wide range of player stats, from general performance metrics like K/D to detailed stats for weapons and vehicles
* **Well Organized Updates:** Efficiently adds new, unique players to the dataset without creating duplicates

## Supported Games
Currently, the scraper supports:
* **Battlefield 4:** use `-g bf4` in command line arguments

**Planned Support:** The project is designed with an extensible architecture to support other Battlefield games, which will be added soon.

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
* `-d, --delay`: Delay in seconds between scraping cycles (default: 0)
* `-b, --batch`: Number of players per batch to write to the dataset (default: 1)
* `-inf, --infinite`: Run scraper in endless mode. You can stop it with `Ctrl+C`

### Usage Example
To run scraper for Battlefield 4 in endless mode with 60-second delay between each cycle, use this command:
```bash
python run.py -o dataset.csv -g bf4 -d 60 -inf
```
The output will be saved to a file named `dataset.csv`

## Data Collected
The scraper gathers a wide array of statistics, stored in a single row per player in the final dataset. This includes:

* **General Performance Metrics:** K/D ratio, accuracy, score per minute, etc
* **Weapon Statistics:** Performance with different weapons
* **Vehicle Statistics:** Performance with different vehicles
* **Game Mode Performance:** Statistics across different game modes
* **Progressive Stats:** Rank and unlock progress