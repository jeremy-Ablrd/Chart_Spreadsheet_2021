import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=4, index_col=1)

df_pec = file.iloc[26:27, 2:14]
df_pec = df_pec.T
var1 = 'Per Capita PEC'

df_fec = file.iloc[27:28, 2:14]
df_fec = df_fec.T
var2 = 'Per Capita FEC'

years = [i for i in df_pec.index]
percapita_pec = [round(e, 2) for e in df_pec['Per capita PEC']]
percapita_fec = [round(e, 2) for e in df_fec['Per capita FEC']]

dict_year_PEC = {'Year': years, 'TOE': percapita_pec, '': [var1 for i in range(0, len(years))]}
dict_year_FEC = {'Year': years, 'TOE': percapita_fec, '': [var2 for i in range(0, len(years))]}
new_df_pec = pd.DataFrame(dict_year_PEC)
new_df_fec = pd.DataFrame(dict_year_FEC)

print(new_df_pec)
print(new_df_fec)

new_df = pd.concat([new_df_pec, new_df_fec], ignore_index=True)
print(new_df)

plt.figure(figsize=(9, 6))
plt.grid(True)
plt.ylim(0, 2.5)
sns.lineplot(x="Year", y="TOE",
             hue="", style="", palette='inferno',
             data=new_df, markers=True, dashes=True)

plt.title('Per Capita PEC vs. Per Capita FEC', fontweight="bold")
path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Trend_PEC-FEC_2010-2021"
plt.savefig(f'{path_savefig}/barchart_spread_PerCapitaPECvsFEC.png', transparent=True, dpi=300)
plt.show()
