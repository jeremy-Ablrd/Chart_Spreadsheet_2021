import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


"""
Line chart:
3 legends : 
- Growth Index for Real GDP
- Growth Index for Population
- Growth Index for PEC

Modified dataframe :
- Calcul the different indexes for obtain 100% for each them at the beginning.
- line required :
    - Population 2014 - 2021
    - Real GDP 2014 - 2021
    - PEC 2014 - 2021
    
Title : Growth Indexes for GDP and PEC
Period : 2014 to 2021
x label : Year
y label : Percentage
"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=4, index_col=1)


def calcul_index(dataframe):
    columns = dataframe.columns[0]
    index = dataframe.index
    value_index_percent = []
    for value in dataframe[f'{columns}']:
        value_index = value / dataframe[f'{columns}'][2014]  # BE CAREFUL index is the year from [2014] to [2021] no [0]
        value_index_percent.append(round(value_index * 100))
    new_df = create_df(index, value_index_percent)
    return new_df


def create_df(index, value):
    global list_name
    global index_name
    df = pd.DataFrame({'Year': index, 'Percentage %': value, "": f'{list_name[index_name]}'})
    return df


list_line = [1, 0, 8]
list_name = ["Growth Index for Real GDP", "Growth Index for Population", "Growth Index for PEC"]
index_name = -1
df_final = pd.DataFrame([])
for line in list_line:
    data = file.iloc[line:line+1, 6:14]
    data = data.T
    index_name += 1
    df_mk = calcul_index(data)
    df_final = pd.concat([df_final, df_mk], ignore_index=True, axis=0)

print(df_final)

plt.figure(figsize=(12, 9))
plt.grid(True)
# plt.ylim(0, 2.5)
sns.lineplot(x="Year", y="Percentage %",
             hue="", style="", palette='inferno',
             data=df_final, markers=True, dashes=True)

plt.title('Growth Indexes for GDP and PEC', fontweight="bold", size=15)

handles, labels = plt.gca().get_legend_handles_labels()
order = [0, 2, 1]
plt.legend([handles[i] for i in order], [labels[i] for i in order])


path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure_GDP"
plt.savefig(f'{path_savefig}/lineChart_spread_GrowthGDP-PEC.png', transparent=True, dpi=300)
plt.show()
