import pandas as pd

df = pd.read_csv('transactions.csv')

top = df[df['STATUS'] == 'OK'].sort_values(by=['SUM'], ascending=False).iloc[:3]
print('The largest payments:\n', top)
print()

total = df[(df['CONTRACTOR'] == 'Umbrella, Inc') & (df['STATUS'] == 'OK')]
print('Total sum for Umbrella, Inc is:', total.sum()['SUM'])

