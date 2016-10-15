import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('AtlanticStormTotalsTable.xlsx', header=1)
df.set_index(df['Year'], inplace=True)
df.drop('Year', axis=1, inplace=True)
cols = df.columns.tolist()
cols = [col.replace(' ', '_') for col in cols]
df.columns = cols

# fig = plt.figure(figsize=(12,8))
# ax = fig.add_subplot(1,1,1)
# ax.bar(df.index, df['Tropical_Storms'], label='Tropical_Storms')
# ax.bar(df.index, df['Hurricanes'], label='Hurricanes', color='green')
# ax.bar(df.index, df['Major_Hurricanes'], label='Major_Hurricanes', color='red')
# ax.set_xlim(1851, 2014)
# ax.set_xlabel('Year')
# ax.set_ylabel('Total')
# plt.legend()
# plt.show()

dftemp = pd.read_csv('global_temperature.csv')
dftemp = dftemp[dftemp['Source'] == 'GCAG'].sort_values('Year')
dfsunspot = pd.read_fwf('SN_y_tot_v2.0.txt', colspecs=[(0,6), (8,13)])
dfsunspot.columns = ['Year', 'Mean']
dfsunspot['Year'] = dfsunspot['Year'].astype(int)
