import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=44, index_col=1)

df_wind = file.iloc[4:5, 2:14]
df_wind = df_wind.T
var1 = df_wind.columns[0]

df_solar = file.iloc[5:6, 2:14]
df_solar = df_solar.T
var2 = df_solar.columns[0]

print(var1)
print(var2)

years = [i for i in df_wind.index]
wind = [round(e, 1) for e in df_wind[var1]]
pv = [round(e, 1) for e in df_solar[var2]]

dict_year_PEC = {'Year': years, 'GWh': wind, '': [var1 for i in range(0, len(years))]}
dict_year_FEC = {'Year': years, 'GWh': pv, '': [var2 for i in range(0, len(years))]}
new_df_wind = pd.DataFrame(dict_year_PEC)
new_df_solar = pd.DataFrame(dict_year_FEC)
new_df = pd.concat([new_df_wind, new_df_solar], ignore_index=True)
print(new_df)

plt.figure(figsize=(9, 6))
ax = sns.barplot(x='Year', y='GWh', hue='', data=new_df, palette='inferno', saturation=0.3)
plt.ylim(0, 8)
plt.legend(loc='upper left')
for container in ax.containers:
    ax.bar_label(container)

plt.title('Electricity Generation from Renewable Energy', fontweight="bold")
path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_Electricity_2010-2021"
plt.savefig(f'{path_savefig}/barchart_spread_ElectGen_RenewEnerg.png', transparent=True, dpi=300)

plt.show()
