import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=44, index_col=1)

df_wind = file.iloc[4:5, 2:14]
df_wind = df_wind.T
df_wind['Wind'] = [round(i, 1) for i in df_wind['Wind']]

df_solar = file.iloc[5:6, 2:14]
df_solar = df_solar.T
df_solar['Solar PV'] = [round(i, 1) for i in df_solar['Solar PV']]

new_df = pd.concat([df_wind, df_solar], axis=1)
new_df.round({'Wind': 1, 'Solar': 0})
new_df = new_df.loc[2013:]
print(new_df.loc[2013:])

sns.set(style='white')
colors = ['#8F79CA', '#518D87']
ax = new_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['black', 'black']

for i, container in enumerate(ax.containers):
    ax.bar_label(container, color=label_color[i], label_type='center')

plt.title('Electricity Generation from Renewable Energy', fontsize=16)
plt.grid(visible=True, axis='y')

plt.xlabel('Year')
plt.xticks(rotation=0)
# plt.xlim(2013, 2021)
plt.ylabel('GWh')


handles, labels = plt.gca().get_legend_handles_labels()
order = [1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_Electricity_2010-2021"
plt.savefig(f'{path_savefig}/barchartDetailled_spread_RenewableEnOnly.png', transparent=True, dpi=300)
plt.show()
