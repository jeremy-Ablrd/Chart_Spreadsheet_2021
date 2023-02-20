import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick


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

sns.set(style='white')
plt.figure(figsize=(12, 9))
plt.grid(True)
plt.ylim(0, 100)
ax = sns.lineplot(x="Year", y="Percentage %",
                  hue=None, style=None, palette='inferno',
                  data=df, markers=True, dashes=True, linewidth=2.7)

ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))

plt.title('Energy System Efficiency', fontweight="bold", fontsize=22)


font_label = 16

plt.xlabel('Year', fontsize=font_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_label)

plt.ylabel("Percentage", fontsize=font_label, fontweight='bold')
plt.yticks(fontsize=font_label)
plt.ylim(0, 100)


path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/Figure_Energy_Sys_Intensity.png', transparent=False, dpi=300)
plt.show()
