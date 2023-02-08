import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

"""
Line chart:
7 legends : 
- Total Domestic Demand for FUEL OIL
- Total Domestic Demand for GASOIL
- Total Domestic Demand for GASOLINE
- Total Domestic Demand for LPG
- Total Domestic Demand for JET A-1
- Total Domestic Demand for Kerosene
- Total Domestic Demand for AVGAS

Title : Total Domestic Demand
Period : 2010 to 2021
x label : Year
y label : Metric Ton (MT)
"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=114, index_col=1)


def round_value(df_, columns_):
    value_percent = []
    for value in df_[f'{columns_}']:
        value_percent.append(int(round(value, 0)))
    dataframe = pd.DataFrame({f'{columns_}': value_percent}, index=df_.index)
    return dataframe


list_fuel = ['for FUEL OIL', 'for GASOIL', 'for GASOLINE', 'for LPG', 'for JET A-1']
list_line = [i for i in range(1, len(list_fuel)+1)]
list_name = ["Total Domestic Demand " + f'{fuel}' for fuel in list_fuel]
index_name = -1

df = pd.DataFrame([])
for line in list_line:
    data = file.iloc[line:line+1, 2:14]
    data = data.T
    columns = data.columns[0]
    data_percent = round_value(data, columns)
    data_new = data_percent.rename(columns={f'{columns}': list_fuel[index_name+1]})
    index_name += 1
    df = pd.concat([df, data_new], axis=1, ignore_index=False)

print(df)

sns.set(style='dark')
colors = ['#573F06', '#704E5D', '#656543', '#AC9C61', '#68220D']
ax = df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['black' for i in range(0, len(list_fuel))]

for i, container in enumerate(ax.containers[:4]):
    ax.bar_label(container, color=label_color[i], label_type='center', padding=0, fontsize=15, fontweight='bold')

for i, container in enumerate(ax.containers[4:]):
    contain_int = np.int_(container.datavalues)
    ax.bar_label(container, labels=contain_int, color=label_color[i], label_type='edge', padding=0, fontsize=15, fontweight='bold')


plt.title('Total Domestic Demand', fontsize=22, fontweight='bold')
plt.grid(visible=True, axis='y')

plt.xlabel('Year', fontsize=16, fontweight='bold')
plt.xticks(rotation=0, fontsize=16, fontweight='bold')
# plt.xlim(2013, 2021)
plt.ylabel('Metric Ton (MT)', fontsize=16, fontweight='bold')
plt.yticks(fontsize=16)


handles, labels = plt.gca().get_legend_handles_labels()
order = [4, 3, 2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order], fontsize=12)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/figure20_DomesticDemandFuel.png', transparent=False, dpi=300)

plt.show()
