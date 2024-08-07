# League of Legends Worlds Championship Data Analysis

**THIS IS STILL A WORK IN PROGRESS!**

## Description
This project analyzes professional League of Legends esports, specifically the Worlds Championship, from 2011 to 2022, to uncover insights on team performance, champion usage, match outcomes, and more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Murillo-ES/lol_worlds_project.git
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate # Or "env\Scripts\activate" if you use Windows
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/pedrocsar/league-of-legends-worlds-20112022-stats/data) and place it in the `data` directory.
2. Run the data loading script:
    ```bash
    python data_loading.py
    ```

## Data
The data used in this project is sourced from the League of Legends Worlds 2011-2022 stats dataset on Kaggle. Ensure the following files are placed in the `data` directory:
    - `champions_stats.csv`
    - `matchs_stats.csv`
    - `players_stats.csv`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please contact [Murillo-ES](https://github.com/Murillo-ES)