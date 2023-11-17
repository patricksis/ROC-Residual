from scipy import odr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import inspect

dfc = pd.read_csv('../data/annotated_genes.csv')

x = dfc['Obs.Log.Mean']
y = dfc['Mean.log10']
sx = dfc['Obs.Log.Std.Dev']
sy = dfc['log10.Std.Dev']

my_data = odr.RealData(x, y, sx=sx, sy=sy)

myodr = odr.ODR(my_data, odr.quadratic)

my_run = myodr.run()

my_run.pprint()


# Access the residuals of the response variable
residuals = my_run.eps
dfc.loc[:, 'odr_y'] = my_run.y
dfc.loc[:, 'Y_residuals'] = residuals

dfc.to_csv('/Users/patricksisler/projects/gilchrist/data/annotated_genes.csv', index=False)

sns.scatterplot(data=dfc, x='odr_y', y='Y_residuals')
sns.displot(data=dfc, x='odr_y', y='Y_residuals')
plt.show()
# If you want to see the residuals
print("Residuals:", residuals)

x_fit = np.linspace(min(x), max(x), 100)

# Compute corresponding y values using the fitted quadratic model
y_fit = my_run.beta[0] * x_fit**2 + my_run.beta[1] * x_fit + my_run.beta[2]

# Scatter plot of your data
sns.scatterplot(x=x, y=y, color='blue', s=8,hue=sy)

# Plot the fitted quadratic function
sns.lineplot(x=x_fit, y=y_fit, color='red', label='Fitted Quadratic')

plt.legend()
plt.savefig('obs_mean_vs_roc_mean.png')
plt.show()
