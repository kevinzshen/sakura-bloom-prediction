#### Preamble ####
# Purpose:
# Author: Kevin Shen
# Date: 30 November 2024
# Contact: kevinzshen3@gmail.com
# License: MIT

### Workspace Setup ###
import pandas as pd
import numpy as np
from statsmodels.regression.mixed_linear_model import MixedLM
from sklearn.model_selection import train_test_split
import joblib
import statsmodels.api as sm


np.random.seed(2620)

# For better formatting in PyCharm's console
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Read data
combined_data = pd.read_csv('../data/02-analysis_data/cleaned_sakura_data.csv')

train_data, test_data = train_test_split(
    combined_data,
    test_size=0.2,
    random_state=2620
)

# Save train and test datasets for later use
train_data.to_csv('../data/02-analysis_data/train_test_data/train_data.csv', index=False)
test_data.to_csv('../data/02-analysis_data/train_test_data/test_data.csv', index=False)


def linear_mixed_effects_model(train_df):
    """
    Fit mixed effects model with:
    - Fixed effects: flower_date, days_to_full_bloom, mean_temp_c, latitude, longitude
    - Random effects: station_id
    Args:
        train_df: DataFrame containing the necessary columns
    Returns:
        Fitted mixed effects model
    """
    # Specify fixed effects
    fixed_effects = sm.add_constant(train_df[['flower_doy', 'mean_temp_c', 'latitude', 'longitude']])

    # Fit the model
    model = MixedLM(
        endog=train_df['days_to_full_bloom'],
        exog=fixed_effects,
        groups=train_df['station_id'],  # Primary random effect
    )

    result = model.fit()

    return result


# Example usage:
# First ensure your data has all required columns
required_cols = ['days_to_full_bloom', 'flower_doy', 'mean_temp_c', 'latitude', 'longitude', 'station_id']

# Fit the model
trained_model = linear_mixed_effects_model(train_data)

# Save model into file
joblib.dump(trained_model, '../models/trained_model.joblib')

# Print summary
print(trained_model.summary())

