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

# -- Chart Setting -- #
sns.set(style='ticks')
plt.figure(figsize=(12, 9))
colors = ['#45B193', '#9E7592']
ax = sns.barplot(x='Year', y='GWh', hue='', data=new_df, palette=colors)


for container in ax.containers:
    ax.bar_label(container, fontsize=18, fontweight='bold')

# ----- Title ----- #
plt.title('Electricity Generation from Renewable Energy', fontsize=21, fontweight="bold")

# ----- Axis ----- #
font_size_label = 18
plt.xlim(2, 12)
plt.xlabel('Year', fontsize=font_size_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_size_label)
plt.ylim(0, 15)
plt.ylabel('GWh', fontsize=font_size_label, fontweight='bold')
plt.yticks(fontsize=font_size_label)

# ----- Legend ----- #
plt.legend(loc='upper left', fontsize=16)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/barchart_spread_ElectGen_RenewEnerg.png', transparent=False, dpi=300)
plt.show()
