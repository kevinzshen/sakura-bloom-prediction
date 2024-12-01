#### Preamble ####
# Purpose:
# Author: Kevin Shen
# Date: 30 November 2024
# Contact: kevinzshen3@gmail.com
# License: MIT

# Workspace Setup
import pandas as pd
import numpy as np
from statsmodels.regression.mixed_linear_model import MixedLM
import statsmodels.api as sm

np.random.seed(2620)

# For better formatting in PyCharm's console
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Read data
combined_data = pd.read_csv('../data/02-analysis_data/cleaned_sakura_data.csv')

# # Convert flower_date and full_bloom_date into datetime format
# combined_data['flower_date'] = pd.to_datetime(combined_data['flower_date'], errors='coerce')
# combined_data['full_bloom_date'] = pd.to_datetime(combined_data['full_bloom_date'], errors='coerce')


def linear_mixed_effects_model(df):
    """
    Fit mixed effects model with:
    - Fixed effects: flower_date, days_to_full_bloom, mean_temp_c, latitude, longitude
    - Random effects: station_id
    Args:
        df: DataFrame containing the necessary columns
    Returns:
        Fitted mixed effects model
    """
    # Specify fixed effects
    fixed_effects = sm.add_constant(df[['flower_doy', 'mean_temp_c', 'latitude', 'longitude']])

    # # Create a simpler random effects structure
    # random_slopes = df[['year']]  # Year as continuous variable

    # Fit the model
    model = MixedLM(
        endog=df['full_bloom_doy'],
        exog=fixed_effects,
        groups=df['station_id'],  # Primary random effect
        # exog_re=random_slopes  # Secondary random effect
    )

    result = model.fit()

    return result


# Example usage:
# First ensure your data has all required columns
required_cols = ['full_bloom_doy', 'flower_doy', 'mean_temp_c', 'latitude', 'longitude', 'station_id']

# Fit the model
model_result = linear_mixed_effects_model(combined_data)

# Print summary
print(model_result.summary())

