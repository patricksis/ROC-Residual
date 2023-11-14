import pandas as pd
import numpy as np

# read data
df1 = pd.read_csv('/Users/patricksisler/projects/gilchrist/data/saccharomyces_cerevisiae.max.cds',sep=',',index_col=0)

# Replace zero values with NaN
df1.replace(0, np.nan, inplace=True)

# log transform the data
log_data = np.log10(df1)

# mean and standard deviatoin of the log data
log_mean_obs = log_data.mean(axis=1)
log_std_dev = log_data.std(axis=1)


result_df = pd.DataFrame({'Obs.Log.Mean': log_mean_obs, 'Obs.Log.Std.Dev': log_std_dev})

# Save the DataFrame to CSV
result_df.to_csv('log_obs.csv')







