import pandas as pd

df1 = pd.read_csv('/Users/patricksisler/projects/gilchrist/data/log_obs.csv',sep=',')

df2 = pd.read_csv('/Users/patricksisler/projects/gilchrist/data/gene_expression.txt',sep=',')

# Merge the two DataFrames on 'GeneID'
merged_data = pd.merge(df1, df2, on='GeneID', how='inner')



# Create a new DataFrame with selected columns
combined_data = merged_data[['GeneID', 'Obs.Log.Mean', 'Mean.log10','Obs.Log.Std.Dev','log10.Std.Dev']]

combined_data = combined_data[~combined_data['GeneID'].str.startswith('R')]


#combined_data_cleaned = combined_data.dropna(subset=['Obs.Log.Std.Dev', 'log10.Std.Dev','Obs.Log.Std.Dev','log10.Std.Dev'], how='any')

combined_data_cleaned = combined_data.dropna(how='any')

combined_data_cleaned.to_csv('combined_data_cleaned.csv', index=True)

