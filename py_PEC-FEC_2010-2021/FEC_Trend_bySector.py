import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=229, index_col=1)

# Transport, Service, Resid, Industry, Agri&fish
lignes = [10, 12, 11, 13, 14]

df = pd.DataFrame([])
for ligne in lignes:
    data = file.iloc[ligne:ligne+1, 2:14]
    data = data.T
    columns = data.columns[0]
    data[f'{columns}'] = [round(i, 2) for i in data[f'{columns}']]
    df = pd.concat([df, data], axis=1)

print(df)

sns.set(style='white')
colors = ['#8F79CA', '#518D87']
ax = df.plot(kind='bar', stacked=True, color=None, figsize=(12, 9))

label_color = ['black', 'black', 'black', 'black', 'black']

for i, container in enumerate(ax.containers):
    ax.bar_label(container, color=label_color[i], label_type='center', padding=0)

plt.title('Final Energy Consumption By Sector', fontsize=16)
plt.grid(visible=True, axis='y')

plt.xlabel('Year')
plt.xticks(rotation=0)
# plt.xlim(2013, 2021)
plt.ylabel('GWh')


handles, labels = plt.gca().get_legend_handles_labels()
order = [4, 3, 2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_PEC-FEC_2010-2021"
plt.savefig(f'{path_savefig}/barchartDetailled_spread_FEC_BySector.png', transparent=True, dpi=300)
plt.show()
