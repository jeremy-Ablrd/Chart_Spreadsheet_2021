import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/" \
       "Spreadsheet for the preparation of Energy Reports ver-12.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=299, index_col=1)


def create_dataframe(list_l, list_s):
    df_final = pd.DataFrame([])
    index_col = 0
    for line in list_l:
        df = file.iloc[line:line+1, 2:14].T
        df["Sectors"] = list_s[index_col]
        index_col += 1
        df.rename(columns={df.columns[0]: "CO2 Emissions"}, inplace=True)
        df_final = pd.concat([df_final, df], axis=0, ignore_index=False)
    df_final.reset_index(inplace=True)
    df_final.rename(columns={"index": "Year"}, inplace=True)
    print(df_final)
    return df_final


def create_simple_dataframe(list_l, list_s):
    df_final = pd.DataFrame([])
    for i, line in enumerate(list_l):
        df = file.iloc[line:line + 1, 2:14].T
        # df["Sectors"] = list_s[index_col]
        df.rename(columns={df.columns[0]: list_s[i]}, inplace=True)
        df_final = pd.concat([df_final, df], axis=1, ignore_index=False)
    # df_final.reset_index(inplace=True)
    # df_final.rename(columns={"index": "Year"}, inplace=True)
    print(df_final)
    return df_final


list_line = [3, 21, 13, 28, 35, 40]
list_sector = ["Electricity Generation", "Transports", "Service", "Industrial", "Residential", "Artisanal & Fishing"]
# concat_dataframe = create_dataframe(list_line, list_sector)
concat_dataframe = create_simple_dataframe(list_line, list_sector)


yrs = concat_dataframe.index.tolist()
print(yrs)


l0 = concat_dataframe[list_sector[0]].tolist()
l1 = concat_dataframe[list_sector[1]].tolist()
l2 = concat_dataframe[list_sector[2]].tolist()
l3 = concat_dataframe[list_sector[3]].tolist()
l4 = concat_dataframe[list_sector[4]].tolist()
l5 = concat_dataframe[list_sector[5]].tolist()

color = ['#A90057', '#EA263A', '#FD3D10', '#FD8801', '#FFB001', '#FEED01']
# blue ['#103B6E', '#1D6BBA', '#33B3F2']

labels = []
for sector in list_sector:
    labels.append(sector)

fig, ax = plt.subplots(figsize=(12, 9))
ax.stackplot(yrs, l0, l1, l2, l3, l4, l5, labels=labels, colors=color)
ax.set_title("Estimation of Seychelles CO2 Emissions from Energy Use", fontsize=16)
# ax.legend(loc='upper left')
handles, labels = plt.gca().get_legend_handles_labels()
order = [5, 4, 3, 2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order], loc='upper left')

ax.grid(visible=True, axis="y", linestyle='--', color='#E2DEE0')
ax.set_ylabel("Metric Ton")
ax.set_xlabel("Year")
ax.set_ylim(0, 600000)
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure"
plt.savefig(f'{path_savefig}/CO2_emission.png', transparent=True, dpi=300)

plt.show()

# -------- Display Figure -------- #

# sns.set_theme(style="whitegrid")
#
# # Plot the distribution of clarity ratings, conditional on carat
# sns.lineplot(x="Year", y="CO2 Emissions", hue="Sectors", data=concat_dataframe,
#              palette="Blues")
#
# plt.show()
