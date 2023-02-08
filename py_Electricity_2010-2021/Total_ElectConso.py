import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=69, index_col=1)

df = file.iloc[8:9, 2:14]
df = df.T
print(df)

years = [i for i in df.index]
electricity_conso_PUC = [round(e) for e in df['Total for PUC Consumers']]

dict_year_elec = {'Year': years, 'Electricity Consumption by PUC [GWh]': electricity_conso_PUC}
new_df = pd.DataFrame(dict_year_elec)

# --------- Chart Setting --------- #
plt.figure(figsize=(12, 9))
sns.set(style='dark')
plt.grid(visible=True, axis='y')
colors = "#FFC404"
ax = sns.barplot(x=new_df['Year'], y=new_df['Electricity Consumption by PUC [GWh]'], color=colors,)
for container in ax.containers:
    ax.bar_label(container, fontsize=16, fontweight='bold')

# --------- Title --------- #
plt.title('Total National Electricity Consumption', fontsize=23, fontweight='bold')


# --------- Axis --------- #
font_size_label = 18
plt.xlabel('Year', fontsize=font_size_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_size_label)
plt.ylim(0, 450)
plt.ylabel('GWh', fontsize=font_size_label, fontweight='bold')
plt.yticks(fontsize=font_size_label)


path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/Figure7_Total_ElectConso.png', transparent=False, dpi=300)
plt.show()

