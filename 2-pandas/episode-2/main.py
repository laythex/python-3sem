import matplotlib.pyplot as plt
import pandas as pd

dfg = pd.read_csv('flights.csv').groupby('CARGO')

cargo = dfg.groups.keys()
flights = dfg['CARGO'].count()
prices = dfg['PRICE'].sum()
weights = dfg['WEIGHT'].sum()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].pie(flights, labels=cargo)
axs[1].pie(prices, labels=cargo)
axs[2].pie(weights, labels=cargo)

axs[0].set_title('Total flights')
axs[1].set_title('Total prices')
axs[2].set_title('Total weights')

plt.savefig('cargo.png')
plt.show()
