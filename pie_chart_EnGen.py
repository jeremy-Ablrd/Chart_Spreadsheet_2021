import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *

path = "C:/Users/jerem/PycharmProjects/pythonProject/Infography/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Electricity Stat-2021", header=39)

# create Dataframe "df" for the table concerned [ELECTRICITY GENERATION MIX IN PUC]
df = file.iloc[0:4, 0:2]

sum_fuel = df['GWh'][0] + df['GWh'][1]

sum_fuel = pd.DataFrame(data=[('Fuel Oil & Gasoil', sum_fuel)], columns=['Technology', 'GWh'])
auto_prod = pd.DataFrame(data=[('Auto-producer', 65.5)], columns=['Technology', 'GWh'])
new_df = pd.concat([df, auto_prod, sum_fuel], axis=0, ignore_index=True)

new_df = new_df.drop([0, 1], axis=0)

total = pd.DataFrame(data=[('Total', sum(new_df['GWh']))], columns=['Technology', 'GWh'])
new_df1 = pd.concat([new_df, total], axis=0, ignore_index=True)

new_df1['Share'] = [i/new_df1['GWh'][len(new_df1)-1] for i in new_df1['GWh']]

new_df_sorted = new_df1[0:len(new_df1)-1].sort_values('GWh', ascending=False, ignore_index=True)


print(f"Main DataFrame:\n{df}")
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

colors_share = ['#566573', '#a3a3a3', '#f97316', '#16a34a']
gap = (0, 0.0, 0.0, 0.0)
wedges1 = {'linewidth': 1, 'edgecolor': 'white'}
text1 = {'fontsize': 19, 'color': 'black'}

# Call function figure(length, width):
figure(12, 9)

# Call function pie_chart(x, labels, colors, explode)
pie_chart(value_percent, energy_key, colors_share, gap, label_dist=1.1, wedge_prop=wedges1, text_prop=text1)

# Call function print_text(x, y, txt, fontsize, color, verti_align, horiz_align, bbox=None)
print_text(-0.5, 0, str(value_percent[0]) + "%", 37, "black", 'top', 'center')     #Fuel oil
print_text(0.55, 0.35, str(value_percent[1]) + "%", 25, "black", 'top', 'center')
print_text(1.75, 0.18, f"({str(value_percent[2])}" + "%)", 19, "black", 'top', 'center')         #Wind
print_text(1.85, 0.09, f"({str(value_percent[3])}" + "%)", 19, "black", 'top', 'center',)       #Solar

path_savefig = "C:/Users/jerem/Desktop/Chart_spreadsheet/Chart"
plt.savefig(f'{path_savefig}/piechart_spread_EnGen.png', transparent=True, dpi=300)
plt.show()
