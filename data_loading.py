import os
import logging
import pandas as pd


def setup_logging():
    """
    This function will setup our 'logging' module to our preferences.
    """

    logging.basicConfig(level=logging.INFO, format='%(asctime)s \
- %(levelname)s - %(message)s')


def load_csv(folder_name: str, csv_name: str) -> pd.DataFrame:
    """
    This function loads a specific CSV using pandas 'read_csv' function.

    Parameters:
        folder_name (str): Name of the folder where the csv is currently in.
        csv_name (str): CSV's name **without the '.csv' particle**.

    Returns:
        A pd.DataFrame with the CSV's content.
    """

    dir_path = os.path.dirname(__file__)
    csv_path = os.path.join(dir_path, f'{folder_name}', f'{csv_name}.csv')

    try:
        csv = pd.read_csv(csv_path)
        logging.info(f'{csv_name} loaded succesfully.')
        return csv
    except FileNotFoundError as e:
        logging.error(f'Error loading {csv_name}: "{e}"')
        print('Please check if the folder and csv names are correct.')


def load_raw_data():
    """
    Loads our raw data.
    """

    champions_stats = load_csv('data', 'champions_stats')
    matchs_stats = load_csv('data', 'matchs_stats')
    players_stats = load_csv('data', 'players_stats')

    return champions_stats, matchs_stats, players_stats


def load_clean_data():
    """
    Loads our clean data.
    """

    champions_stats = load_csv(
        'clean_data',
        'champions_stats'
    )
    champions_stats_s1_to_s3 = load_csv(
        'clean_data',
        'champions_stats_s1_to_s3'
    )
    champions_stats_s4_to_s9 = load_csv(
        'clean_data',
        'champions_stats_s4_to_s9'
    )
    champions_stats_s10_above = load_csv(
        'clean_data',
        'champions_stats_s10_above'
    )
    matchs_stats = load_csv(
        'clean_data',
        'matchs_stats'
    )
    players_stats = load_csv(
        'clean_data',
        'players_stats'
    )
    players_stats_s1_to_s3 = load_csv(
        'clean_data',
        'players_stats_s1_to_s3'
    )
    players_stats_s4_to_s9 = load_csv(
        'clean_data',
        'players_stats_s4_to_s9'
    )
    players_stats_s10_above = load_csv(
        'clean_data',
        'players_stats_s10_above'
    )

    return (
        champions_stats,
        champions_stats_s1_to_s3,
        champions_stats_s4_to_s9,
        champions_stats_s10_above,
        matchs_stats,
        players_stats,
        players_stats_s1_to_s3,
        players_stats_s4_to_s9,
        players_stats_s10_above
    )


if __name__ == "__main__":
    pass
