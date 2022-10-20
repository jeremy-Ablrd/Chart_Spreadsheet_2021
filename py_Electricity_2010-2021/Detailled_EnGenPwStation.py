import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Book1.xlsx"
# apprendre a collecter plus facilement les doner de ce type de tableau

# ---------- DataFrame for YEAR ---------- #
file_year = pd.read_excel(path, 'Generation-Summary (2)', header=38)
file_year = file_year.iloc[3:12, 0].astype('int')
print(file_year)

# ---------- DataFrame for DATA POWER STATION ---------- #
# year = [int(y) for y in file_year]
file = pd.read_excel(path, 'Generation-Summary (2)', header=38, index_col=None, usecols=[3, 7, 13])
df = pd.DataFrame(file.iloc[3:12])

df.rename(columns={"Sub-total": "Vic-B Newport",
                   "Sub-total.1": "Vic-C Roche Caiman",
                   "Sub-total.2": "BSA-Praslin"}, inplace=True)

first_col = df.pop("Vic-C Roche Caiman")
df.insert(0, "Vic-C Roche Caiman", first_col)


# ---------- New DataFrame for DATA POWER STATION with YEAR ---------- #
new_df = pd.concat((file_year, df), axis=1)
new_df.set_index(keys="Unnamed: 0", inplace=True)

for n_columns in new_df.columns:
    new_df[f"{n_columns}"] = [round(i, 2) for i in new_df[f"{n_columns}"]]

print(new_df)

# ---------- CONFIG CHART ---------- #
# set seaborn plotting aesthetics
sns.set(style='white')
# create stacked bar chart
colors = ['#8F79CA', '#518D87', '#22A21F']

# df = new_df.set_index('Year')
ax = new_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['black', 'black', 'black']

# Add value on each bar
for i, container in enumerate(ax.containers):
    ax.bar_label(container, color=label_color[i], label_type='center')

# add overall title
plt.title('Electricity Generation by PUC with HFO/LFO', fontsize=16)
plt.grid(visible=True, axis='y')
# add axis titles
plt.xlabel('Year')
plt.ylabel('GWh')
# rotate x-axis labels
# plt.ylim(200, 500)
plt.xticks(rotation=0)

# reordering the labels
handles, labels = plt.gca().get_legend_handles_labels()
# specify order
order = [2, 1, 0]
# pass handle & labels lists along with order as below
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_Electricity_2010-2021"
plt.savefig(f'{path_savefig}/barchartDetailled_spread_PowerStation.png', transparent=True, dpi=300)

plt.show()
