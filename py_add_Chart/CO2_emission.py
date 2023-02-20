import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/" \
       "Spreadsheet for the preparation of Energy Reports ver-12.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=299, index_col=1)


def create_simple_dataframe(list_l, list_s):
    df_final = pd.DataFrame([])
    for i, line in enumerate(list_l):
        df = file.iloc[line:line + 1, 2:14].T
        df.rename(columns={df.columns[0]: list_s[i]}, inplace=True)
        df_final = pd.concat([df_final, df], axis=1, ignore_index=False)
    print(df_final)
    return df_final


list_line = [3, 21, 13, 28, 35, 40]
list_sector = ["Electricity Generation", "Transports", "Service", "Industrial", "Residential", "Agriculture"]

concat_dataframe = create_simple_dataframe(list_line, list_sector)


yrs = concat_dataframe.index.tolist()
print(yrs)


l0 = concat_dataframe[list_sector[0]].tolist()
l1 = concat_dataframe[list_sector[1]].tolist()
l2 = concat_dataframe[list_sector[2]].tolist()
l3 = concat_dataframe[list_sector[3]].tolist()
l4 = concat_dataframe[list_sector[4]].tolist()
l5 = concat_dataframe[list_sector[5]].tolist()

color = ['#FFC404', '#A48273', '#52B48E', '#DD8452', '#4C72B0', '#F98B05']
# blue ['#103B6E', '#1D6BBA', '#33B3F2']

labels = []
for sector in list_sector:
    labels.append(sector)

sns.set(style='white')

l_all = l0, l1, l2, l3, l4, l5

fig, ax = plt.subplots(figsize=(12, 9))
ax.stackplot(yrs, l_all, labels=labels, colors=color)
ax.set_title("Estimation of Seychelles CO2 Emissions from Energy Use", fontsize=20, fontweight='bold')

handles, labels = plt.gca().get_legend_handles_labels()
order = [5, 4, 3, 2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order], loc='upper left', fontsize=12)

font_label = 16
ax.grid(visible=True, axis="y", linestyle='--', color='#E2DEE0')

ax.set_xlabel("Year", fontsize=font_label,  fontweight='bold')
ax.set_ylabel("Metric Ton", fontsize=font_label, fontweight='bold')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
ax.set_ylim(0, 600000)


# path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
# plt.savefig(f'{path_savefig}/figure27_CO2_emission.png', transparent=False, dpi=300)

plt.show()
