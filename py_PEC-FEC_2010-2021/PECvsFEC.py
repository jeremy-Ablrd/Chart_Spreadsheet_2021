import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=4, index_col=1)

df_pec = file.iloc[7:8, 2:14]
df_pec = df_pec.T
var1 = 'PEC'

df_fec = file.iloc[17:18, 2:14]
df_fec = df_fec.T
var2 = 'FEC'

years = [i for i in df_pec.index]
pec_conso = [round(e, 1) for e in df_pec['PEC']]
fec_conso = [round(e, 1) for e in df_fec['FEC']]

dict_year_PEC = {'Year': years, 'kTOE': pec_conso, '': [var1 for i in range(0, len(pec_conso))]}
dict_year_FEC = {'Year': years, 'kTOE': fec_conso, '': [var2 for i in range(0, len(fec_conso))]}
new_df_pec = pd.DataFrame(dict_year_PEC)
new_df_fec = pd.DataFrame(dict_year_FEC)

new_df = pd.concat([new_df_pec, new_df_fec], ignore_index=True)
print(new_df)

plt.figure(figsize=(9, 6))
ax = sns.barplot(x='Year', y='kTOE', hue='', data=new_df, palette='inferno')
plt.ylim(0, 200)
#
#
for container in ax.containers:
    ax.bar_label(container)

plt.title('Primary Energy vs. Final Energy Consumption', fontweight="bold")          #y=1.06
# # plt.suptitle('or Total Primary Energy Supply (TPES)', y=0.92, x=0.51)
path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_PEC-FEC_2010-2021"
plt.savefig(f'{path_savefig}/barchart_spread_PECvsFEC.png', transparent=True, dpi=300)
plt.show()

