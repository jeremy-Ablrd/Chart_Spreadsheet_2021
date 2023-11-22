import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
Legend :
 - Auto-producers in commerce
 - Private services
 - Public services
 
Title : 
 - Electricity Consumption in the Service Sector
 
Unit : 
 - GWh
"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=69, index_col=1)

list_line = [29, 30, 28]

df_final = pd.DataFrame([])
for line in list_line:
    df = file.iloc[line:line+1, 2:14]
    df = df.T.astype(float)             # convert to flot for make sure all number have the same type (float).
    df = df.round(0)
    df_final = pd.concat([df_final, df], axis=1)

print(df_final)

sns.set(style='white')
colors = ['#8F79CA', '#518D87']
ax = df_final.plot(kind='bar', stacked=True, color=None, figsize=(12, 9))

label_color = ['black' for i in range(0, len(list_line))]
# label_color.append('#903B3F')
#
for i, container in enumerate(ax.containers[:]):
    ax.bar_label(container, color=label_color[i], label_type='center', fontsize=16, fontweight='bold')

plt.title('Electricity Consumption in the Service Sector', fontsize=22, fontweight='bold')
plt.grid(visible=False, axis='y')

font_label = 16
plt.xlabel('Year', fontsize=font_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_label)
plt.ylabel('GWh', fontsize=font_label, fontweight='bold')
plt.yticks(fontsize=font_label)

handles, labels = plt.gca().get_legend_handles_labels()
order = [i for i in reversed(range(0, len(list_line)))]
print(order)
plt.legend([handles[i] for i in order], [labels[i] for i in order], fontsize=12)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart_Energy_Report"
plt.savefig(f'{path_savefig}/figure43_ElectConso_Service.png', transparent=False, dpi=300)
plt.show()

