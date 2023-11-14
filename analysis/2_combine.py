import pandas as pd

df1 = pd.read_csv('/Users/patricksisler/projects/gilchrist/analysis/log_obs.csv',sep=',')

df2 = pd.read_csv('/Users/patricksisler/projects/gilchrist/data/gene_expression.txt',sep=',')

# Merge the two DataFrames on 'GeneID'
merged_data = pd.merge(df1, df2, on='GeneID', how='inner')

# Create a new DataFrame with selected columns
new_df = merged_data[['GeneID', 'Obs.Log.Mean', 'Mean.log10','Obs.Log.Std.Dev','log10.Std.Dev']]

new_df.to_csv('combined_data.csv', index=True)

