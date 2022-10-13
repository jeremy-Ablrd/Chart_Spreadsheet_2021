import pandas as pd
from Function_PieChart_Electricity_Gen import *
from Function_PieChart_PEC_FEC import *

# -------  Config for SECTORIAL ENERGY CONSUMPTION ------- #

# Config Dict for DataFrame
data = {'Domestic': 138745369,
        'Industry & Commercial': 207422855,
        'Government': 55489598 - 1019437,
        'Street Lights':  1019437}

# Make a DataFrame
df = pd.DataFrame(data.values(), index=data.keys(), columns=['TOE'])
df = df.sort_values('TOE', ascending=False)
print(df)

# Congig Data for Chart
sectors = df.index.tolist()
generation = df['TOE']
colors1 = ['#00b386', '#269393', '#ffb833', 'red']
explode1 = (0, 0, 0, 0)
label_dist = 1.1
wedge = {'linewidth': 1, 'edgecolor': 'white'}
text = {'fontsize': 19, 'color': 'black'}

# Value in percent
values_percent = []
for data in generation:
    operation = round((data/sum(generation)) * 100, 1)
    values_percent.append(operation)

print(list(zip(sectors, values_percent)))

# ------- GENERATE GRAPHIQUE ------- #

figure(12, 9)
pie_chart(generation, sectors, colors1, explode1, label_dist, wedge, text)

print_text(0, -0.4, str(values_percent[0]) + "%", 37, "black", 'top', 'center')
print_text(-0.3, 0.5, str(values_percent[1]) + "%", 36, "black", 'top', 'center')
print_text(0.6, 0.3, f"{str(values_percent[2])}" + "%", 27, "black", 'top', 'center')
print_text(1.93, 0.06, f"({str(values_percent[3])}" + "%)", 19, "black", 'top', 'center',)

# ------- SAVE FIGURE & SHOW------- #
path_savefig = "C:/Users/jerem/Desktop/Chart_spreadsheet/Chart"
plt.savefig(f'{path_savefig}/piechart_spread_EnConso.png', transparent=True, dpi=300)
plt.show()
