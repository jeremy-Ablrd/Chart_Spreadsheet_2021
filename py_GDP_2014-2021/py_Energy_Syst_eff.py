import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
Line chart:
1 legends : 
- Energy System Efficiency

Title : Energy System Efficiency
Period : 2010 to 2021
x label : Year
y label : Percentage
"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=4, index_col=1)


def percent(df_, columns_):
    value_percent = []
    for value in df_[f'{columns_}']:
        value_percent.append(int(round(value * 100, 0)))
    dataframe = pd.DataFrame({'Year': df_.index, f'{columns_}': value_percent})
    return dataframe


list_line = [31]
list_name = ['Energy System Efficiency']
index_name = -1

df = pd.DataFrame([])
for line in list_line:
    data = file.iloc[line:line+1, 2:14]
    data = data.T
    print(data)
    columns = data.columns[0]
    data_percent = percent(data, columns)
    data_new = data_percent.rename(columns={f'{columns}': "Percentage %"})
    data_new[""] = list_name[index_name + 1]
    index_name += 1
    df = pd.concat([df, data_new], axis=0, ignore_index=True)

print(df)

plt.figure(figsize=(12, 9))
plt.grid(True)
plt.ylim(50, 65)
sns.lineplot(x="Year", y="Percentage %",
             hue=None, style=None, palette='inferno',
             data=df, markers=True, dashes=True)

plt.title('Energy System Efficiency', fontweight="bold", size=15)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure_GDP"
plt.savefig(f'{path_savefig}/lineChart_spread_EnergySysIntensity.png', transparent=True, dpi=300)
plt.show()
