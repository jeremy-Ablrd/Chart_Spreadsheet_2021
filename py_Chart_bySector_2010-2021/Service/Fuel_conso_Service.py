import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
Legend :
 - Kerosene
 - Gasoil
 - LPG

Unit : TOE
"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=188, index_col=1)

list_line = [16, 17, 19]

df_final = pd.DataFrame([])
for line in list_line:
    df = file.iloc[line:line + 1, 2:14]
    df = df.T.astype(float)  # convert to flot for make sure all number have the same type (float).
    df = df.round(0)
    df_final = pd.concat([df_final, df], axis=1)

print(df_final)

sns.set(style='white')
colors = ['#A25B75', '#C44E52', '#903B3F']
ax = df_final.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['black' for i in range(0, len(list_line))]
# label_color.append('#903B3F')
#
for i, container in enumerate(ax.containers[:]):
    ax.bar_label(container, color=label_color[i], label_type='center', padding=0.9)

plt.title('Fuel Consumption in the Service Sector', fontsize=16)
plt.grid(visible=True, axis='y')

plt.xlabel('Year')
plt.xticks(rotation=0)
#plt.ylim(0, 320)
plt.ylabel('TOE')

handles, labels = plt.gca().get_legend_handles_labels()
order = [i for i in reversed(range(0, len(list_line)))]
print(order)
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure_Sector/Service"
plt.savefig(f'{path_savefig}/BarchartDetailled_spread_FuelConso_Service.png', transparent=True, dpi=300)
plt.show()
