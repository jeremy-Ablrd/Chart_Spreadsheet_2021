import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=69, index_col=1)

# Losses (techn & non-tech), street lights, PUC Station'sConso, Govern(inclu. PUC), Resid, Industry and Commerce
df_losses = file.iloc[10:11, 2:14]
df_losses = df_losses.T

df_street = file.iloc[3:4, 2:14]
df_street = df_street.T

df_PUCstat = file.iloc[9:10, 2:14]
df_PUCstat = df_PUCstat.T

df_government = file.iloc[2:3, 2:14]
df_government = df_government.T

df_residential = file.iloc[:1, 2:14]
df_residential = df_residential.T

df_indus_commerce = file.iloc[1:2, 2:14]
df_indus_commerce = df_indus_commerce.T

new_df = pd.concat([df_indus_commerce, df_residential, df_government, df_losses, df_PUCstat, df_street], axis=1)
for columns in new_df.columns:
    new_df[f'{columns}'] = [round(i, 2) for i in new_df[f'{columns}']]

print(new_df)


sns.set(style='white')
colors = ['#8F79CA', '#518D87']
ax = new_df.plot(kind='bar', stacked=True, color=None, figsize=(12, 9))

label_color = ['black', 'black', 'black', 'black', 'black', 'red']

for i, container in enumerate(ax.containers):
    ax.bar_label(container, color=label_color[i], label_type='center', padding=0)

plt.title('Electricity Consumption by Sector (includ. losses)', fontsize=16)
plt.grid(visible=True, axis='y')

plt.xlabel('Year')
plt.xticks(rotation=0)
# plt.xlim(2013, 2021)
plt.ylabel('GWh')


handles, labels = plt.gca().get_legend_handles_labels()
order = [5, 4, 3, 2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_Electricity_2010-2021"
plt.savefig(f'{path_savefig}/barchartDetailled_spread_ElecConsoLosses.png', transparent=True, dpi=300)
plt.show()
