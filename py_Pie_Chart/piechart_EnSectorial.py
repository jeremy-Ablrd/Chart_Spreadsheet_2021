import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *
from Function_PieChart_PEC_FEC import *

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/" \
       "Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=99)             # Already DataFrame by pandas

dataframe = file.iloc[0:8, 0:3]
dataframe.drop([1, 2, 3], axis=0, inplace=True)
dataframe.replace(to_replace='Artisanal Fishing', value='AGRICULTURE', inplace=True)
df_transport = dataframe.iloc[0:4]

sector_label = [i for i in dataframe['SECTOR'].str.title()]
data_share = [i for i in dataframe['Share']]

colors1 = ['#A48273', '#52B48E', '#4C72B0', '#DD8452', '#F98B05']
explode1 = (0, 0, 0, 0, 0)
label_dist = 1.1
wedge = {'linewidth': 1, 'edgecolor': 'white'}
text = {'fontsize': 25, 'color': 'black'}

print(dataframe)

figure(12, 9)
pie_chart(data_share, sector_label, colors1, explode1, label_dist, wedge, text, auto_nb='%1.1f%%')

path_savefig = "C:/Users/jerem/Desktop/Chart_spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/Figure37_piechart_EnSectorial.png', transparent=False, dpi=300)

plt.show()
