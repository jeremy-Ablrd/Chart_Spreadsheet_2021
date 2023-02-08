import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 2013 to 2021

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Commissioned PV Systems List 221103.xlsx"
file = pd.read_excel(path, sheet_name="Sheet2", header=88)

df = file.iloc[1:10, 1:6]
df.drop(["Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)
# df.set_index([pd.Index([i for i in range(2013, 2022)])], inplace=True)
print(df)

df_year = df["Year"].astype('int')
df_T_annual = df["Total Annual Installed Capacity"]
df_cumul = df['Cumulative Capacity']

new_df = pd.DataFrame([df_T_annual]).T
new_df2 = pd.DataFrame([df_cumul]).T

new_df.index = [i for i in range(2013, 2022)]
new_df2.reset_index(inplace=True, drop=True)

print(new_df)
print(new_df2)

colors_bar = ['#8F79CA']
color_line = ['#57106E']

plt.figure(figsize=(12, 9))

ax1 = new_df[f'Total Annual Installed Capacity'].plot(kind='bar', color=colors_bar)
ax2 = new_df2[f'Cumulative Capacity'].plot(kind='line', color=color_line)

label_color = ['black']

for i, container_a in enumerate(ax1.containers[:3]):
    ax1.bar_label(container_a, color=label_color[i], label_type='edge', padding=0, fontsize='large')

plt.title("Development of Distributed Generation Solar PV on Mahe, Praslin & La Digue", fontsize=16)

# X config
plt.xlabel("Year")
# Y config
plt.ylabel("kWh")
plt.grid(visible=True, axis='y')


plt.legend()
print(type(ax1))

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021"
plt.savefig(f'{path_savefig}/capacity_installed.png', transparent=True, dpi=300)
plt.show()
