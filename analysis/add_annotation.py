import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


combined_data = pd.read_csv('combined_data.csv', sep=',')

# Drop rows with missing values in both 'Obs.Log.Std.Dev' and 'log10.Std.Dev' columns
combined_data_cleaned = combined_data.dropna(subset=['Obs.Log.Std.Dev', 'log10.Std.Dev'], how='any')

plt.scatter(combined_data['Obs.Log.Std.Dev'], combined_data['log10.Std.Dev'])
plt.xlabel('Observed Std. Dev.')
plt.ylabel('Log10 Std. Dev.')
plt.title('Scatter Plot')
plt.show()

# Assuming 'Obs.Log.Std.Dev' is the independent variable and 'log10.Std.Dev' is the dependent variable
X = combined_data_cleaned['Obs.Log.Std.Dev']  # Independent variable
y = combined_data_cleaned['log10.Std.Dev']    # Dependent variable

# Add a constant term to the independent variable (intercept)
X = sm.add_constant(X)

# equation
# y = 0.2112 + 0.0682x
# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the predicted values
y_predicted = model.predict(X)


# Calculate the residuals
residuals = y - y_predicted

plt.scatter(y_predicted, residuals)
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.title('Residuals vs. Predicted values')
plt.show()

# Print the summary statistics of the regression
print(model.summary())

obs_std_dev = combined_data_cleaned['Obs.Log.Std.Dev']
log10_std_dev = combined_data_cleaned['log10.Std.Dev']

plt.scatter(range(len(obs_std_dev)), obs_std_dev, color='blue', label='Obs Log Std Dev')
plt.scatter(range(len(log10_std_dev)), log10_std_dev, color='red', label='ROC log Std Dev')

plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Obs.Log Std Dev and ROC log Std Dev')

plt.legend()
plt.show()

plt.scatter(combined_data_cleaned['Obs.Log.Std.Dev'], combined_data_cleaned.index)
plt.show()
