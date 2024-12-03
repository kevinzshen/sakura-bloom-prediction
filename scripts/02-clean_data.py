#### Preamble ####
# Purpose:
# Author: Kevin Shen
# Date: 30 November 2024
# Contact: kevinzshen3@gmail.com
# License: MIT
# Pre-requisites:
#  - `pandas` must be installed (pip install pandas)
#  -  01-download_data.py must have been run

### Workspace Setup ###
import pandas as pd

# For better formatting in PyCharm's console
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Read data
sakura_modern = pd.read_csv('../data/01-raw_data/sakura-modern.csv')
temps = pd.read_csv('../data/01-raw_data/temperatures-modern.csv')

# Convert the flower_date to datetime
sakura_modern['flower_date'] = pd.to_datetime(sakura_modern['flower_date'])
sakura_modern['flower_month'] = sakura_modern['flower_date'].dt.strftime('%b')  # Converts to month abbreviations.

# Process temperature data
temps = temps[['station_id', 'year', 'month', 'mean_temp_c']]

# Merge sakura and temperature data
merged_data = pd.merge(
    sakura_modern,
    temps,
    left_on=['station_id', 'year', 'flower_month'],
    right_on=['station_id', 'year', 'month'],
    how='inner'
)

# Clean the data:
# 1. Remove any rows with missing values
merged_data = merged_data.dropna(subset=[
    'flower_doy',
    'full_bloom_doy',
    'flower_date',
    'full_bloom_date',
    'mean_temp_c',
    'latitude',
    'longitude'
])

# 2. Create a feature for days between flowering and full bloom
merged_data['days_to_full_bloom'] = (
    merged_data['full_bloom_doy'] - merged_data['flower_doy']
)

# 3. Add year and month columns for potential seasonality analysis
# merged_data['flower_year'] = merged_data['flower_date'].dt.year
# merged_data['flower_month'] = merged_data['flower_date'].dt.month

# 4. Keep only the relevant columns for our analysis
final_data = merged_data[[
    'station_id',
    'year',
    'latitude',
    'longitude',
    'flower_doy',
    'full_bloom_doy',
    'mean_temp_c',
    'days_to_full_bloom'
]].copy()

# 5. Add basic data quality checks
assert not final_data.duplicated().any(), "Duplicate rows found in final dataset"
assert not final_data.isnull().any().any(), "Missing values found in final dataset"
assert (final_data['days_to_full_bloom'] >= 0).all(), "Negative days to full bloom found"

# Save the cleaned dataset
final_data.to_csv('../data/02-analysis_data/cleaned_sakura_data.csv', index=False)
final_data.to_parquet('../data/02-analysis_data/cleaned_sakura_data.parquet')

# Print basic statistics about the cleaned dataset
print("\nCleaned Dataset Summary:")
print(f"Number of observations: {len(final_data)}")
print(f"Number of unique stations: {final_data['station_id'].nunique()}")
print(f"Year range: {final_data['year'].min()} to {final_data['year'].max()}")
print("\nDescriptive Statistics:")
print(final_data.describe())