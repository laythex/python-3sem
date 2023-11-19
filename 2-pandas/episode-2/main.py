import matplotlib.pyplot as plt
import pandas as pd

dfg = pd.read_csv('flights.csv')
dfg['COUNT'] = 1
dfg = dfg.drop(['Unnamed: 0'], axis=1)
dfg.groupby('CARGO').sum().plot.pie(subplots=True, figsize=(20, 10))

plt.savefig('cargo.png')
plt.show()
