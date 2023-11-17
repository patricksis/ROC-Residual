import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

combined_data_cleaned = pd.read_csv('combined_data_cleaned.csv',sep=',')

# Drop rows with missing values in both 'Log Mean' and 'Mean.log10' columns
#combined_data_cleaned = combined_data.dropna(subset=['Obs.Log.Mean', 'Mean.log10'], how='any')

X = combined_data_cleaned['Obs.Log.Mean']  # Independent variable
y = combined_data_cleaned['Mean.log10']  # Dependent variable

# Add a constant term to the independent variable
X = sm.add_constant(X)

model = sm.OLS(y, X)

results = model.fit()


print(results.summary())

# Predicted values
predicted = results.predict()

# Observed vs. Predicted
plt.figure(figsize=(8, 6))
plt.scatter(predicted, y, alpha=0.5, color='blue')
plt.title('Observed vs. Predicted')
plt.xlabel('Predicted')
plt.ylabel('Observed')
plt.savefig('../figures/mean_obs_vs_rog.png')
plt.show()

#print(combined_data['Obs Log Mean'].isnull().sum())
#print(combined_data['Obs Log Mean'].isin([np.inf, -np.inf]).sum())

