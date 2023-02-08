import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Energy Data-PUC-2021.xlsx"
file = pd.read_excel(path, sheet_name="Summary-PUC-2013-2021")
file_summary = pd.read_excel(path, sheet_name="Summary-PUC-2013-2021", header=2, usecols=[17])


# Funtion for convert kWh to GWh
def convert_to_gwh(dataf: DataFrame):
    dataf_col = dataf.columns[0]
    if not dataf_col == "Year":
        dataf[f"{dataf_col}"] = dataf[f"{dataf_col}"]/1000
        # for data in dataf[f"{dataf_col}"]:
        #     data = data/100
        return dataf
    return dataf


# = ("Mahe", [4, 13, 17]), ("Praslin", [4, 13, 17]), ("Mahe + Praslin", [30, 39, 15])
list_nom = ["Year", "Mahe", "Praslin", "Mahe + Praslin"]
list_data = [[4, 13, 1], [4, 13, 18], [17, 26, 14], [30, 39, 17]]           # [30, 39, 15]

df_final = pd.DataFrame([])
for i, li in enumerate(list_data):
    df = file.iloc[li[0]:li[1], li[2]:li[2]+1]
    df = df.rename(columns={f"{df.columns[0]}": f"{list_nom[i]}"}).astype('int')
    df.index = [i for i in range(len(df))]
    # df = convert_to_gwh(df)
    df_final = pd.concat([df_final, df], axis=1)

df_final.set_index(keys="Year", drop=True, inplace=True)

print(df_final)


sns.set(style='white')
colors = ['#0700CC', '#00A805', '#EE0609']
ax = df_final.plot(kind='line', stacked=False, color=colors, figsize=(12, 9))

# label_color = ['black' for c in range(len(df.columns))]
#
# for i, container in enumerate(ax.containers[:3]):
#     ax.bar_label(container, color=label_color[i], label_type='center', padding=0)

plt.title('Technical and Non-technical Losses on Mahe and Praslin', fontsize=16)
plt.grid(visible=True, axis='y')

plt.xlabel('Year')
plt.xticks(rotation=0)
# plt.xlim(2009, 2022)
plt.ylabel("Percentage %")
plt.ylim(0, 20)

handles, labels = plt.gca().get_legend_handles_labels()
order = [i for i in reversed(range(0, len(df_final.columns)))]
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/figure4_Tech-NonTech_PrasMah.png', transparent=False, dpi=300)
plt.show()
