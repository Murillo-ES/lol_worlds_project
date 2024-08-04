import os
import logging
import pandas as pd


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s \
- %(levelname)s - %(message)s')


def load_data():
    # Current working directory
    script_dir = os.path.dirname(__file__)

    # File paths
    champions_stats_path = os.path.join(
        script_dir,
        'data',
        'champions_stats.csv'
    )
    matchs_stats_path = os.path.join(script_dir, 'data', 'matchs_stats.csv')
    players_stats_path = os.path.join(script_dir, 'data', 'players_stats.csv')

    # Load datasets
    try:
        champions_stats = pd.read_csv(champions_stats_path)
        logging.info('champions_stats loaded succesfully.')
    except FileNotFoundError as e:
        logging.error(f'Error loading champions_stats: "{e}".')
        logging.error('Please check that the champions_stats file path is \
correct.')
        champions_stats = None

    try:
        matchs_stats = pd.read_csv(matchs_stats_path)
        logging.info('matchs_stats loaded succesfully.')
    except FileNotFoundError as e:
        logging.error(f'Error loading matchs_stats: "{e}".')
        logging.error('Please check that the matchs_stats file path is \
correct.')
        matchs_stats = None

    try:
        players_stats = pd.read_csv(players_stats_path)
        logging.info('players_stats loaded succesfully.')
    except FileNotFoundError as e:
        logging.error(f'Error loading players_stats: "{e}".')
        logging.error('Please check that the players_stats file path is \
correct.')
        players_stats = None

    return champions_stats, matchs_stats, players_stats


if __name__ == "__main__":
    setup_logging()
    champions_stats, matchs_stats, players_stats = load_data()

    if (champions_stats is not None and
            matchs_stats is not None and
            players_stats is not None):
        logging.info('All datasets loaded succesfully.\n')
    else:
        logging.error('One or more datasets failed to load. Please check the \
    errors above.')
