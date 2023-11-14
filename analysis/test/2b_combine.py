import pandas as pd

# Assuming you have two DataFrames: df1 and df2
# And that 'GeneID' is the common column you want to merge on

# Load the DataFrames (replace 'path/to/your/file.csv' with the actual file paths)
df1 = pd.read_csv('../data/annotated_genes.csv')
df2 = pd.read_csv('../data/gene_data_with_go_terms.csv')

# Merge the DataFrames on the 'GeneID' column
merged_df = pd.merge(df1, df2, on='GeneID', how='outer')

# The 'how' parameter can be 'inner', 'outer', 'left', or 'right' depending on the type of join you need:
# 'inner' - Only rows with matching keys in both DataFrames are included in the result (intersection).
# 'outer' - All rows from both DataFrames are included, with NaN in places where one DataFrame is missing a key (union).
# 'left' - All rows from the left DataFrame are included in the result, with NaN in places where the right DataFrame is missing a key.
# 'right' - All rows from the right DataFrame are included in the result, with NaN in places where the left DataFrame is missing a key.

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('GO_combined_data.csv', index=False)
