import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from Function_PieChart_Electricity_Gen import *

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Seychelles Energy Balance For 2021 - ver3.xlsx"
file = pd.read_excel(path, sheet_name="Electricity Stat-2021", header=40)

# create Dataframe "df" for the table concerned [ELECTRICITY GENERATION MIX IN PUC]
df = file.iloc[0:4, 0:2]

sum_fuel = df['GWh'][0] + df['GWh'][1]

sum_fuel = pd.DataFrame(data=[('Fuel Oil & Gasoil', sum_fuel)], columns=['Technology', 'GWh'])
# auto_prod = pd.DataFrame(data=[('Auto-producer', 65.5)], columns=['Technology', 'GWh'])
new_df = pd.concat([df, sum_fuel], axis=0, ignore_index=True)

new_df = new_df.drop([0, 1], axis=0)

total = pd.DataFrame(data=[('Total', sum(new_df['GWh']))], columns=['Technology', 'GWh'])
new_df1 = pd.concat([new_df, total], axis=0, ignore_index=True)

new_df1['Share'] = [i/new_df1['GWh'][len(new_df1)-1] for i in new_df1['GWh']]

new_df_sorted = new_df1[0:len(new_df1)-1].sort_values('GWh', ascending=False, ignore_index=True)
df_sorted = df.sort_values('GWh', ascending=False, ignore_index=True)
df_sorted['Share'] = [element/sum(df_sorted['GWh']) for element in df_sorted['GWh']]

print(f"Main DataFrame:\n{df}")
print()
print(f"Main DataFrame sorted:\n{df_sorted}")
print()
print(f"DataFrame update:\n{new_df1}")
print()
print(f"DataFrame sorted:\n{new_df_sorted}")

share = new_df_sorted['Share']
# Change Share to percentage
share_percent = []
for i in share.values:
    share_percent.append(round(i*100, 1))
share_percent = np.array(share_percent)

energy_key = [i for i in new_df_sorted['Technology']]
value_percent = share_percent
print(energy_key)
print(value_percent)

colors_share1 = ['#007F7F', '#FAD335', '#A3B825']
colors_share2 = ['#007F7F', '#42A0A0', '#FAD335', '#A3B825']
wedges1 = {'linewidth': 1, 'edgecolor': 'white'}
text1 = {'fontsize': 19, 'color': 'black'}

sns.set(style='white')


ax1 = new_df_sorted.plot(kind='pie', y='GWh', counterclock=False, labels=None, colors=colors_share1, figsize=(9, 9))
plt.title("Elect Generation Summary")
plt.ylabel('')
ax1.get_legend().remove()
path_savefig = "/Correction_chart_Energy_Report"
plt.savefig(f'{path_savefig}/Electricity_generation_summary.png', transparent=True, dpi=300)

ax = df_sorted.plot(kind='pie', y='GWh', counterclock=False, labels=None, colors=colors_share2, figsize=(9, 9))
plt.title("Elect Generation Fuel Breakdown")
plt.ylabel('')
ax.get_legend().remove()

path_savefig = "/Correction_chart_Energy_Report"
plt.savefig(f'{path_savefig}/Electricity_generation_Fuel_break.png', transparent=True, dpi=300)

# plt.show()

"""# Call function figure(length, width):
figure(12, 9)

# Call function pie_chart(x, labels, colors, explode)
pie_chart(value_percent, energy_key, colors_share, gap, label_dist=1.1, wedge_prop=wedges1, text_prop=text1)

# Call function print_text(x, y, txt, fontsize, color, verti_align, horiz_align, bbox=None)
print_text(-0.5, 0, str(value_percent[0]) + "%", 37, "black", 'top', 'center')     #Fuel oil
print_text(0.55, 0.35, str(value_percent[1]) + "%", 25, "black", 'top', 'center')
print_text(1.75, 0.18, f"({str(value_percent[2])}" + "%)", 19, "black", 'top', 'center')         #Wind
print_text(1.85, 0.09, f"({str(value_percent[3])}" + "%)", 19, "black", 'top', 'center',)       #Solar


plt.show()"""
