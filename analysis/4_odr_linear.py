from scipy import odr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../data/combined_data.csv')
dfc = df.dropna(subset=['Obs.Log.Mean', 'Mean.log10', 'Obs.Log.Std.Dev', 'log10.Std.Dev'], how='any')

x = dfc['Obs.Log.Mean']
y = dfc['Mean.log10']
sx = dfc['Obs.Log.Std.Dev']
sy = dfc['log10.Std.Dev']

my_data = odr.RealData(x, y, sx=sx, sy=sy)

myodr = odr.ODR(my_data, odr.unilinear)

myoutput = myodr.run()

myoutput.pprint()

# plt.errorbar(x, y, xerr=sx, yerr=sy, fmt='o', color='blue', label='Data')


# Scatter plot of your data
sns.scatterplot(x=x, y=y, color='blue', label='Data')

# Fitted line
sns.lineplot(x=x, y=myoutput.beta[0] * x + myoutput.beta[1], color='red', label='Fitted Line')

plt.legend()
plt.show()
