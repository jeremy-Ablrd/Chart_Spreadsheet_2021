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

plt.figure(figsize=(9, 6))
ax = sns.barplot(x=new_df['Year'], y=new_df['Electricity Consumption by PUC [GWh]'], palette='YlOrRd')


plt.title('Total Electricity Consumption\n by PUC (excluding auto-producers)', fontweight="bold")

for container in ax.containers:
    ax.bar_label(container)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_Electricity_2010-2021"
plt.savefig(f'{path_savefig}/barchart_spread_TotalConso.png', transparent=True, dpi=300)
plt.show()
