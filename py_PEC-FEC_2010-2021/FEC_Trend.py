import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=4, index_col=1)

df = file.iloc[17:18, 2:14]
df = df.T
print(df)

years = [i for i in df.index]
fec_conso = [round(e, 1) for e in df['FEC']]

dict_year_elec = {'Year': years, 'kTOE': fec_conso}
new_df = pd.DataFrame(dict_year_elec)
print(new_df)

sns.set(style='white')
plt.figure(figsize=(12, 9))
ax = sns.barplot(x=new_df['Year'], y=new_df['kTOE'], palette='winter_r')

for container in ax.containers:
    ax.bar_label(container, fontweight='bold', fontsize=16)

font_label = 16
plt.xlabel('Year', fontsize=font_label, fontweight='bold')
plt.xticks(fontsize=font_label)
plt.ylabel('kTOE', fontsize=font_label, fontweight='bold')
plt.yticks(fontsize=font_label)
plt.ylim(0, 120)

plt.title('Final Energy Consumption', fontsize=22, fontweight="bold")          #y=1.06
# plt.suptitle('or Total Primary Energy Supply (TPES)', y=0.92, x=0.51)

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart_Energy_Report"
plt.savefig(f'{path_savefig}/figure36_Trend_FEC-2010-2021.png', transparent=False, dpi=300)
plt.show()
