#### Preamble ####
# Purpose: Downloads and saves the sakura flowering datasets from GitHub
# Author: Kevin Shen
# Date: 2 December 2024
# Contact: kevinzshen3@gmail.com
# License: MIT
# Pre-requisites:
#  - `pandas` must be installed (pip install pandas)
#  - `requests` must be installed (pip install requests)

### Workspace Setup ###
import requests
import pandas as pd
from pathlib import Path


def create_folders():
    """Create necessary folders if they don't exist."""
    Path("../data/01-raw_data").mkdir(parents=True, exist_ok=True)


def download_github_csv(url, output_path):
    """
    Download a CSV file from GitHub and save it locally.

    Args:
        url (str): Raw GitHub URL for the CSV file
        output_path (str): Local path where the file should be saved
    """
    try:
        # Get the raw content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Save the content to a file
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded: {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")


def main():
    # Create folders
    create_folders()

    # Define the URLs for the raw data files
    sakura_modern_url = "https://raw.githubusercontent.com/tacookson/data/refs/heads/master/sakura-flowering/sakura-modern.csv"
    sakura_historical_url = "https://raw.githubusercontent.com/tacookson/data/refs/heads/master/sakura-flowering/sakura-historical.csv"
    temperature_modern_url = "https://raw.githubusercontent.com/tacookson/data/refs/heads/master/sakura-flowering/temperatures-modern.csv"


    # Define output paths
    sakura_modern_output = "../data/01-raw_data/sakura_modern.csv"
    sakura_historical_output = "../data/01-raw_data/sakura_historical.csv"
    temperature_modern_output = "../data/01-raw_data/temperatures_modern.csv"

    # Download the files
    download_github_csv(sakura_modern_url, sakura_modern_output)
    download_github_csv(sakura_historical_url, sakura_historical_output)
    download_github_csv(temperature_modern_url, temperature_modern_output)

    # Verify the downloads by reading and displaying the first few rows
    try:
        sakura_m_df = pd.read_csv(sakura_modern_output)
        sakura_h_df = pd.read_csv(sakura_historical_output)
        temp_df = pd.read_csv(temperature_modern_output)

        print("\nFirst few rows of Sakura Modern dataset:")
        print(sakura_m_df.head())
        print("\nFirst few rows of Sakura Historical dataset:")
        print(sakura_h_df.head())
        print("\nFirst few rows of Temperature Modern dataset:")
        print(temp_df.head())

    except Exception as e:
        print(f"Error verifying downloads: {e}")


if __name__ == "__main__":
    main()