import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
Line chart:
3 legends : 
- Growth Index for Real GDP
- Growth Index for Population
- Growth Index for PEC


Title : Growth Indexes for GDP and PEC
Period : 2014 to 2021
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


list_line = [4, 5, 15]
list_name = ['Growth Index for Real GDP', 'Growth Index for Population', 'Growth Index for PEC']
index_name = -1

df = pd.DataFrame([])
for line in list_line:
    data = file.iloc[line:line+1, 6:14]
    data = data.T
    columns = data.columns[0]
    data_percent = percent(data, columns)
    data_new = data_percent.rename(columns={f'{columns}': "Percentage %"})
    data_new[""] = list_name[index_name + 1]
    index_name += 1
    df = pd.concat([df, data_new], axis=0, ignore_index=True)

print(df)

plt.figure(figsize=(12, 9))
plt.grid(True)
# plt.ylim(0, 2.5)
sns.lineplot(x="Year", y="Percentage %",
             hue="", style="", palette='inferno',
             data=df, markers=True, dashes=True)

print(df.index)

plt.title('Growth Indexes for GDP and PEC', fontweight="bold", size=15)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure_GDP"
plt.savefig(f'{path_savefig}/lineChart_spread_GrowthGDP-PEC.png', transparent=True, dpi=300)
plt.show()
