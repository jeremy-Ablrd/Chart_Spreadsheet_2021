import pandas as pd
from Function_PieChart_Electricity_Gen import *
from Function_PieChart_PEC_FEC import *

# -------  Config for SECTORIAL ENERGY CONSUMPTION ------- #

# Config Dict for DataFrame
data = {'Domestic': 138745369,
        'Industry & Commerce': 207422855,
        'Government': 55489598 - 1019437,
        'Street Lights':  1019437}

# Make a DataFrame
df = pd.DataFrame(data.values(), index=data.keys(), columns=['TOE'])
df = df.sort_values('TOE', ascending=False)
print(df)

# Congig Data for Chart
sectors = df.index.tolist()
generation = df['TOE']
colors1 = ['#DD8452', '#4C72B0', '#55A868', '#F7AD19']      # industry, residential, government, streetlights
explode1 = (0, 0, 0, 0)
label_dist = 1.1
wedge = {'linewidth': 1, 'edgecolor': 'white'}
text = {'fontsize': 27, 'color': 'black'}

# Value in percent
values_percent = []
for data in generation:
    operation = round((data/sum(generation)) * 100, 1)
    values_percent.append(operation)

print(list(zip(sectors, values_percent)))

# ------- GENERATE GRAPHIQUE ------- #

figure(14, 9)
pie_chart(generation, sectors, colors1, explode1, label_dist, wedge, text)

print_text(0, -0.4, str(values_percent[0]) + "%", 37, "black", 'top', 'center')
print_text(-0.3, 0.5, str(values_percent[1]) + "%", 36, "black", 'top', 'center')
print_text(0.6, 0.3, f"{str(values_percent[2])}" + "%", 29, "black", 'top', 'center')
print_text(2.23, 0.07, f"({str(values_percent[3])}" + "%)", 25, "black", 'top', 'center',)

# ------- SAVE FIGURE & SHOW------- #
path_savefig = "C:/Users/jerem/Desktop/Chart_spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/piechart_spread_EnConso.png', transparent=False, dpi=300)
plt.show()
