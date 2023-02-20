import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
Line chart:
3 legends : 
- Energy Intensity of the GDP


Title : Energy Intensity of the GDP
Period : 2010 to 2021
x label : Year
y label : TOE/MSR
"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=4, index_col=1)


def percent(df_, columns_):
    value_percent = []
    for value in df_[f'{columns_}']:
        value_percent.append(value)
    dataframe = pd.DataFrame({'Year': df_.index, f'{columns_}': value_percent})
    return dataframe


list_line = [30]
list_name = ['Energy Intensity of the GDP']
index_name = -1

df = pd.DataFrame([])
for line in list_line:
    data = file.iloc[line:line+1, 6:14]
    data = data.T
    print(data)
    columns = data.columns[0]
    data_percent = percent(data, columns)
    data_new = data_percent.rename(columns={f'{columns}': "TOE/MSR"})
    data_new[""] = list_name[index_name + 1]
    index_name += 1
    df = pd.concat([df, data_new], axis=0, ignore_index=True)

print(df)

font_label = 16

sns.set(style='white')
plt.figure(figsize=(12, 9))
plt.grid(True)
# plt.ylim(0, 2.5)
sns.lineplot(x="Year", y="TOE/MSR",
             hue="", style=None, color=None, palette=None,
             data=df, markers=False, dashes=False, linewidth=6.0)

plt.title('Energy Intensity of the GDP', fontweight="bold", size=22)
plt.xlabel('Year', fontsize=font_label, fontweight='bold')
plt.xticks(fontsize=font_label)

plt.yticks(fontsize=font_label)
plt.ylabel('TOE/MSR', fontsize=font_label, fontweight='bold')
plt.ylim(0, 9)

plt.legend(fontsize=12)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/Figure_EnergyIntensityGDP.png', transparent=False, dpi=300)
plt.show()
