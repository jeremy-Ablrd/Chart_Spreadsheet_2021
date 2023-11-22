import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

"""
legend :
 - Kerosene, 
 - Gasoil (vehicles in public services),
 - LPG for cooking,
 - Electricity
"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=188, index_col=1)

list_line = [23, 16, 17, 19]

df_final = pd.DataFrame([])
for line in list_line:
    df = file.iloc[line:line+1, 2:14]
    df = df.T.astype(float)             # convert to flot for make sure all number have the same type (float).
    df = df.round(0)
    df_final = pd.concat([df_final, df], axis=1)

print(df_final)

opacity = 99
sns.set(style='white')
# colors = [f'#FFC404{opacity}', f'#AC9C61{opacity}', f'#704E5D{opacity}', f'#EA8555{opacity}']
ax = df_final.plot(kind='bar', stacked=True, color=None, figsize=(12, 9))

label_color = ['black' for i in range(0, len(list_line)-1)]
label_color.append('#903B3F')

for i, container in enumerate(ax.containers[:3]):
    ax.bar_label(container, fontsize=16, fontweight='bold', color=label_color[i], label_type='center')

for i, container in enumerate(ax.containers[3:]):
    container_int = np.int_(container.datavalues)
    ax.bar_label(container, labels=container_int, fontsize=16, fontweight='bold', color=label_color[i], label_type='edge')

plt.title('Final Energy Consumption in the Service Sector', fontsize=22, fontweight='bold')
plt.grid(visible=False, axis='y')

font_label = 16
plt.xlabel('Year', fontsize=font_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_label)
plt.ylabel('TOE', fontsize=font_label, fontweight='bold')
plt.yticks(fontsize=font_label)


handles, labels = plt.gca().get_legend_handles_labels()
order = [i for i in reversed(range(0, len(list_line)))]
print(order)
plt.legend([handles[i] for i in order], [labels[i] for i in order], fontsize=12)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart_Energy_Report"
# plt.savefig(f'{path_savefig}/figure42_trend-Service.png', transparent=False, dpi=300)
plt.show()
