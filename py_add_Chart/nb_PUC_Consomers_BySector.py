import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-11.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=59, index_col=1)


df = file.iloc[0:4, 2:14]
df = df.T.astype('int')
print(df)

sns.set(style='white')
colors = ['#4C72B0', '#DD8452', '#55A868', '#F7AD19']
ax = df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['black' for c in range(len(df.columns))]

font_size_value = 15

for i, container_residential in enumerate(ax.containers[0:1]):
    ax.bar_label(container_residential, color=label_color[i], label_type='edge',
                 fontsize=font_size_value, fontweight='bold', padding=-100)

for i, container_gov_com in enumerate(ax.containers[1:3]):
    ax.bar_label(container_gov_com, color=label_color[i], label_type='center',
                 fontsize=font_size_value, fontweight='bold', padding=0)

for i, container_streetlight in enumerate(ax.containers[3:]):
    container_int = np.int_(container_streetlight.datavalues)
    ax.bar_label(container_streetlight, color=label_color[i], labels=container_int, label_type='edge',
                 fontsize=font_size_value, fontweight='bold', padding=0)

# --------- Title --------- #
plt.title('Number of Electricity Consumers by Sector', fontsize=23, fontweight='bold')
plt.grid(visible=True, axis='y')

# --------- Axis --------- #
font_size_label = 16
plt.xlabel('Year', fontsize=font_size_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_size_label)
plt.ylim(15000, 45000)
plt.ylabel('Number of Electricity Consumption', fontsize=font_size_label, fontweight='bold')
plt.yticks(fontsize=font_size_label)

# --------- Legends --------- #
handles, labels = plt.gca().get_legend_handles_labels()
order = [i for i in reversed(range(0, len(df.columns)))]
plt.legend([handles[i] for i in order], [labels[i] for i in order], fontsize=font_size_label)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/Figure6_nb_PUC_Consumers_bySector.png', transparent=False, dpi=300)
plt.show()
