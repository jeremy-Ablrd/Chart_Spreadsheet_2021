import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=4, index_col=1)

df = file.iloc[7:8, 2:14]
df = df.T


years = [i for i in df.index]
pec_conso = [round(e, 1) for e in df['PEC']]

dict_year_elec = {'Year': years, 'kTOE': pec_conso}
new_df = pd.DataFrame(dict_year_elec)
print(new_df)

plt.figure(figsize=(9, 6))
ax = sns.barplot(x=new_df['Year'], y=new_df['kTOE'], palette='viridis_r')

for container in ax.containers:
    ax.bar_label(container)

plt.title('Primary Energy Consumption', fontweight="bold", y=1.06)
plt.suptitle('or Total Primary Energy Supply (TPES)', y=0.92, x=0.51)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_PEC-FEC_2010-2021"
plt.savefig(f'{path_savefig}/barchart_spread_PEC.png', transparent=True, dpi=300)
plt.show()
