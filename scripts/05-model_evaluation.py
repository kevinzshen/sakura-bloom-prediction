#### Preamble ####
# Purpose: Evaluate the performance of the mixed effects model in predicting sakura full bloom dates
# Author: Kevin Shen
# Date: 30 November 2024
# Contact: kevinzshen3@gmail.com
# License: MIT
# Pre-requisites:
#  - `pandas` must be installed (pip install pandas)
#  - `numpy` must be installed (pip install numpy)
#  - `joblib` must be installed (pip install joblib)
#  - `statsmodels` must be installed (pip install statsmodels)
#  - `scikit-learn` must be installed (pip install scikit-learn)
#  - `matplotlib` must be installed (pip install matplotlib)
#  - `seaborn` must be installed (pip install seaborn)

### Workspace Setup ###
import pandas as pd
import numpy as np
import joblib
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the model and test data
model = joblib.load('../models/trained_model.joblib')
test_data = pd.read_csv('../data/02-analysis_data/train_test_data/test_data.csv')

# Prepare test data features
X_test = sm.add_constant(test_data[['flower_doy', 'mean_temp_c', 'latitude', 'longitude']])

# Make predictions
y_pred = model.predict(X_test)
y_true = test_data['days_to_full_bloom']

# Calculate performance metrics
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

print(f"Model Performance Metrics:")
print(f"Root Mean Square Error: {rmse:.2f} days")
print(f"Mean Absolute Error: {mae:.2f} days")
print(f"R-squared Score: {r2:.3f}")

# Create residual plot
residuals = y_true - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Days to Full Bloom')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.savefig('../figures/residual_plot.png')
plt.close()

# Create predicted vs actual plot
plt.figure(figsize=(10, 6))
plt.scatter(y_true, y_pred, alpha=0.5)
plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
plt.xlabel('Actual Days to Full Bloom')
plt.ylabel('Predicted Days to Full Bloom')
plt.title('Predicted vs Actual Days to Full Bloom')
plt.savefig('../figures/predicted_vs_actual.png')
plt.close()

# Distribution of prediction errors
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True)
plt.xlabel('Prediction Error (days)')
plt.ylabel('Count')
plt.title('Distribution of Prediction Errors')
plt.savefig('../figures/prediction_error_distribution.png')
plt.close()

# Optional: Analyze errors by geographical location
plt.figure(figsize=(12, 6))
plt.scatter(test_data['longitude'], test_data['latitude'],
           c=abs(residuals), cmap='YlOrRd')
plt.colorbar(label='Absolute Prediction Error (days)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Prediction Errors by Location')
plt.savefig('../figures/geographical_errors.png')
plt.close()

metrics_df = pd.DataFrame({
    'Metric': ['Root Mean Square Error', 'Mean Absolute Error', 'R-squared'],
    'Value': [f"{rmse:.2f} days", f"{mae:.2f} days", f"{r2:.3f}"],
    'Description': [
        'Average magnitude of prediction errors',
        'Average absolute prediction error',
        'Proportion of variance explained by the model'
    ]
})

# Save the metrics to a CSV file
metrics_df.to_csv('../data/03-model_evaluation_data/model_metrics.csv', index=False)