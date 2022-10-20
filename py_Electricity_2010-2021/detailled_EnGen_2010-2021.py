import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create Dataframe
"""df = pd.DataFrame({'Day': ['Mon', 'Tue', 'Wed', 'Thur', 'Fri'],
                   'Morning': [44, 46, 49, 59, 54],
                   'Evening': [33, 46, 50, 49, 60]})"""

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=44, index_col=1)

df_fuel = file.iloc[3:4, 2:14]
df_fuel = df_fuel.T
var0 = df_fuel.columns[0]

df_wind = file.iloc[4:5, 2:14]
df_wind = df_wind.T
var1 = df_wind.columns[0]

df_solar = file.iloc[5:6, 2:14]
df_solar = df_solar.T
var2 = df_solar.columns[0]

variable = ['fuel', ]

years = [i for i in df_wind.index]
fuel = [round(e, 1) for e in df_fuel[var0]]
wind = [round(e, 1) for e in df_wind[var1]]
pv = [round(e, 1) for e in df_solar[var2]]

dict_year = {
    'Year': years,
    f'{var0}': fuel,
    f'{var1}': wind,
    f'{var2}': pv,
             }

new_df = pd.DataFrame(dict_year)
print(new_df)

# set seaborn plotting aesthetics
sns.set(style='white')

# create stacked bar chart
colors = ['#221150', '#518D87', '#22A21F']
df = new_df.set_index('Year')
ax = df.plot(kind='bar', stacked=True, color=colors)

# Add value in each bar
# for container in ax.containers[:-1]:
#     ax.bar_label(container)

# add overall title
plt.title('Total Energy Generation', fontsize=12)
plt.grid(visible=True, axis='y')
# add axis titles
plt.xlabel('Year')
plt.ylabel('GWh')

# rotate x-axis labels
plt.ylim(200, 500)
plt.xticks(rotation=0)

# reordering the labels
handles, labels = plt.gca().get_legend_handles_labels()

# specify order
order = [2, 1, 0]

# pass handle & labels lists along with order as below
plt.legend([handles[i] for i in order], [labels[i] for i in order])

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_Electricity_2010-2021"
plt.savefig(f'{path_savefig}/barchartDetailled_spread_TotalElectGen.png', transparent=True, dpi=300)
plt.show()
