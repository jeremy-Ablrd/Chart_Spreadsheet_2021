import numpy
import matplotlib.ticker as mtick

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------- DATA SECTION --------------------------- #

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Analysis of Fuel Import Burden.xlsx"
file = pd.read_excel(path, sheet_name="Sheet1", header=11, index_col=0)

df_analysis = file.iloc[1:9, 0:5]

###
df_analysis.index = numpy.int_(df_analysis.index)
df_analysis = df_analysis * 100

for column in df_analysis:
    series = df_analysis[f'{column}']
    df_analysis[f'{column}'] = [round(i) for i in series]
###

name_lineplot = ['R1 : Share of fuel in import',
                 'R2 : Fuel import burden in GDP',
                 'R3 : Share of net fuel import in total import',
                 'R4 : Net fuel import Burden in GDP']

# to put in a function
df_analysis_rename = pd.DataFrame([])
for i, name in enumerate(name_lineplot):
    df_analysis.rename(columns={f'{df_analysis.columns[i]}': name}, inplace=True)
    df_analysis_rename = pd.concat([df_analysis])

print(df_analysis_rename)

# to put in a function
y_data = []
for i in range(0, len(df_analysis_rename.columns)):
    y_data.append(f'{df_analysis_rename.columns[i]}')

# ----- Config Chart ----- #

color_ = ['#FA1060', '#8800EB', '#3D91E6', '#00E547']
style_ = ['^-', 'o-', 's-', 'x-']
offset = 0.4
font_value = [14, 'bold']

# to put in a function
sns.set(style='white')
plt.figure(figsize=(12, 9))

for j in range(len(name_lineplot)):
    ax = df_analysis_rename[f'{df_analysis_rename.columns[j]}'].plot(kind='line', style=style_[j], color=color_[j])
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))

    for i in range(len(df_analysis_rename[name_lineplot[j]])):
        if j == 1 or j == 3:
            ax.annotate(f"{df_analysis_rename[name_lineplot[j]][df_analysis_rename.index[i]]}%",
                        xy=(df_analysis_rename.index[i],
                            df_analysis_rename[name_lineplot[j]][df_analysis_rename.index[i]] - offset),
                        verticalalignment='top', horizontalalignment='right', fontsize=font_value[0],
                        fontweight=font_value[1])
        else:
            ax.annotate(f"{df_analysis_rename[name_lineplot[j]][df_analysis_rename.index[i]]}%",
                        xy=(df_analysis_rename.index[i],
                            df_analysis_rename[name_lineplot[j]][df_analysis_rename.index[i]] + offset),
                        verticalalignment='bottom', fontsize=font_value[0], fontweight=font_value[1])

plt.grid(axis='y', visible=True)
plt.title('Analysis of Fuel Import Burden', fontsize=22, fontweight='bold')

font_label = [16, 'bold']

plt.xlabel('Year', fontsize=font_label[0], fontweight=font_label[1])
plt.xticks(rotation=0, fontsize=font_label[0])

plt.ylabel('', fontsize=font_label[0], fontweight=font_label[1])
plt.yticks(fontsize=font_label[0])
plt.ylim(0, 28)

plt.legend()

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/figure19_Analysis_fuel_burden.png', transparent=False, dpi=300)

plt.show()
