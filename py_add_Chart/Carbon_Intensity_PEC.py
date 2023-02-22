import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

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
ax = df.plot(kind='line', stacked=False, color=colors, figsize=(12, 9), linewidth=2.7)

# label_color = ['black' for c in range(len(df.columns))]
#
# for i, container in enumerate(ax.containers[:3]):
#     ax.bar_label(container, color=label_color[i], label_type='center', padding=0)


plt.grid(visible=True, axis='both')

plt.title('Carbon Intensity of PEC', fontweight="bold", fontsize=22)


font_label = 16

plt.xlabel('Year', fontsize=font_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_label)

plt.ylabel(f'{unit}', fontsize=font_label, fontweight='bold')
plt.yticks(fontsize=font_label)
plt.ylim(0, 5)

handles, labels = plt.gca().get_legend_handles_labels()
order = [i for i in reversed(range(0, len(df.columns)))]
# plt.legend([handles[i] for i in order], [labels[i] for i in order],)

ax.legend().set_visible(False)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/Figure_Carbon_Intensity_PEC.png', transparent=False, dpi=300)
plt.show()
