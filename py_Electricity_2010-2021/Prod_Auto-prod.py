import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=44, index_col=1)

df = file.iloc[10:11, 2:14]
df = df.T
print(df)

years = [i for i in df.index]
electricity_prod_autoprod = [round(e) for e in df['Production of Auto-producers with LFO']]

dict_year_elec = {'Year': years, 'Electricity Production [GWh]': electricity_prod_autoprod}
new_df = pd.DataFrame(dict_year_elec)

plt.figure(figsize=(9, 6))
ax = sns.barplot(x=new_df['Year'], y=new_df['Electricity Production [GWh]'], palette='Wistia')

for container in ax.containers:
    ax.bar_label(container)

plt.title('Electricity Production by Auto-producers', fontweight="bold")
path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_Electricity_2010-2021"
plt.savefig(f'{path_savefig}/barchart_spread_ProdElect_AutoProd.png', transparent=True, dpi=300)
plt.show()
