import pandas as pd
import statsmodels.api as sm

# Load your data
df = pd.read_csv('../data/go_combined_data.csv')

# One-hot encoding for categorical variables
df_encoded = pd.get_dummies(df, columns=['Chromosome_Number', 'Chromosome_Arm', 'Strand'], drop_first=False)

X_columns = [col for col in df_encoded.columns if 'Chromosome_Number' in col or 'Chromosome_Arm' in col or 'Strand' in col]
selected_variables = ['Strand_D', 'Strand_E', 'Chromosome_Arm_L', 'Chromosome_Arm_R']

X = df_encoded[X_columns]
Y = df_encoded['Y_residuals']
X = X.astype(float)


# Adding a constant to the model
X = sm.add_constant(X)

# Creating and fitting the model
model = sm.OLS(Y, X)
results = model.fit()

with open('../data/multi_model_summary.txt', 'w') as f:
    f.write(results.summary().as_text())

# Printing the summary
print(results.summary())
