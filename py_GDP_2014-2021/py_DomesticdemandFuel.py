import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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

sns.set(style='white')
colors = ['#8F79CA', '#518D87']
ax = df.plot(kind='bar', stacked=True, color=None, figsize=(12, 9))

label_color = ['black' for i in range(0, len(list_fuel))]

for i, container in enumerate(ax.containers):
    ax.bar_label(container, color=label_color[i], label_type='center', padding=0)

plt.title('Total Domestic Demand', fontsize=16)
plt.grid(visible=True, axis='y')

plt.xlabel('Year')
plt.xticks(rotation=0)
# plt.xlim(2013, 2021)
plt.ylabel('Metric Ton (MT)')


handles, labels = plt.gca().get_legend_handles_labels()
order = [4, 3, 2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure_GDP"
plt.savefig(f'{path_savefig}/barchartDetailled_spread_DomesticDemandFuel.png', transparent=True, dpi=300)

plt.show()
