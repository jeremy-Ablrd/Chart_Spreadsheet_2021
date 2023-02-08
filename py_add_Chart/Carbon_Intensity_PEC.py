import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-11.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=295, index_col=1)

line = 48
unit = file.iloc[line:line+1, 1:2]
unit = unit[f"{unit.columns[0]}"][0]
print(unit)
df = file.iloc[line:line+1, 2:14]
df = df.T
print(df)

sns.set(style='white')
colors = ['#518D87']
ax = df.plot(kind='line', stacked=False, color=colors, figsize=(12, 9))

# label_color = ['black' for c in range(len(df.columns))]
#
# for i, container in enumerate(ax.containers[:3]):
#     ax.bar_label(container, color=label_color[i], label_type='center', padding=0)

plt.title('Carbon Intensity of Primary Energy Consumption', fontsize=16)
plt.grid(visible=True, axis='y')

plt.xlabel('Year')
plt.xticks(rotation=0)
# plt.xlim(2009, 2022)
plt.ylabel(f'{unit}')
plt.ylim(2.9, 3.5)


handles, labels = plt.gca().get_legend_handles_labels()
order = [i for i in reversed(range(0, len(df.columns)))]
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/figure_new1"
plt.savefig(f'{path_savefig}/Carbon_Intensity_PEC-linechart.png', transparent=True, dpi=300)
plt.show()
