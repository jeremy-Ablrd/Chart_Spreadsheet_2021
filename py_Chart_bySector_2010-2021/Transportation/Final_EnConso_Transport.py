import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
legend :
 - Air Transportation
 - Marine Transportation
 - Road Transportation
"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=114, index_col=1)

list_line = [34, 46, 50]
list_name = ["Road Transports", "Air Transportation", "Marine Transportation"]

df_final = pd.DataFrame([])
for line in list_line:
    df = file.iloc[line:line+1, 2:14]
    df = df.T.astype(float)             # convert to flot for make sure all number have the same type (float).
    df = df.round(0)
    df_final = pd.concat([df_final, df], axis=1)

df_final.columns = list_name            # renommer la colonne pour éviter d'utiliser les boucles
print(df_final)

opacity = 99
sns.set(style='white')
colors = [f'#44933E{opacity}', f'#312E5F{opacity}', f'#164C5F{opacity}']
ax = df_final.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['black' for i in range(0, len(list_line))]
# label_color.append('#903B3F')
#
for i, container in enumerate(ax.containers[:]):
    ax.bar_label(container, fontsize=16, fontweight='bold', color=label_color[i], label_type='center', padding=0.9)

plt.title('Final Energy Consumption in the Transport Sector', fontsize=22, fontweight='bold')
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
plt.savefig(f'{path_savefig}/figure40_Trend-Transport.png', transparent=False, dpi=300)
plt.show()
