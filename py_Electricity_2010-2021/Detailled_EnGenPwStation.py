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
file = pd.read_excel(path, 'Generation-Summary (2)', header=38, index_col=None, usecols=[3, 7, 15])
df = pd.DataFrame(file.iloc[3:12])

df.rename(columns={"Sub-total": "Vic-B Newport",
                   "Sub-total.1": "Vic-C Roche Caiman",
                   "LFO.2": "BSA-Praslin"}, inplace=True)

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
sns.set(style='darkgrid')      # white, dark, whitegrid, darkgrid, ticks
# create stacked bar chart
colors = ['#53585C', '#8F9FA8', '#B4B4B8']

# df = new_df.set_index('Year')
ax = new_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['white', 'black', 'black']

# Add value on each bar
for i, container in enumerate(ax.containers):
    cont_int = np.int_(container.datavalues)
    print(container.datavalues)
    ax.bar_label(container, color=label_color[i], labels=cont_int, label_type='center', fontsize=18, fontweight='bold')

font_size_label = 17

plt.title('Electricity Generation by PUC with HFO/LFO', fontsize=22)
plt.xlabel('Year', fontsize=font_size_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_size_label)
plt.ylabel('GWh', fontsize=font_size_label, fontweight='bold')
plt.yticks(fontsize=font_size_label)

# reordering the labels
handles, labels = plt.gca().get_legend_handles_labels()
# specify order
order = [2, 1, 0]
# pass handle & labels lists along with order as below
plt.legend([handles[i] for i in order], [labels[i] for i in order], fontsize=16)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/barchartDetailled_spread_PowerStation.png', transparent=False, dpi=300)

plt.show()
