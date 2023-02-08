import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Spreadsheet for the preparation of Energy Reports ver-9_Update_returned_4Oct22.xlsx"
file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=69, index_col=1)

# Losses (techn & non-tech), street lights, PUC Station'sConso, Govern(inclu. PUC), Resid, Industry and Commerce
df_losses = file.iloc[10:11, 2:14]
df_losses = df_losses.T

df_street = file.iloc[3:4, 2:14]
df_street = df_street.T

df_PUCstat = file.iloc[9:10, 2:14]
df_PUCstat = df_PUCstat.T

df_government = file.iloc[2:3, 2:14]
df_government = df_government.T

df_residential = file.iloc[:1, 2:14]
df_residential = df_residential.T

df_indus_commerce = file.iloc[1:2, 2:14]
df_indus_commerce = df_indus_commerce.T

new_df = pd.concat([df_indus_commerce, df_residential, df_government, df_losses, df_PUCstat, df_street], axis=1)
for columns in new_df.columns:
    new_df[f'{columns}'] = [round(i, 2) for i in new_df[f'{columns}']]

print(new_df)

sns.set(style='dark')
colors = ['#DD8452', '#4C72B0', '#55A868', '#EE0609', '#B4B4B8', '#F7AD19']
ax = new_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['black' for i in range(len(new_df))]
font_size_label = 16

for i, container in enumerate(ax.containers[:5]):
    cont_int = np.int_(container.datavalues)
    ax.bar_label(container, color=label_color[i], labels=cont_int, label_type='center',  fontsize=font_size_label, fontweight='bold', padding=0)

for i, container in enumerate(ax.containers[5:]):
    cont_int = np.round(container.datavalues, 2)
    ax.bar_label(container, color='black', labels=cont_int, label_type='edge',  fontsize=font_size_label, fontweight='bold', padding=0)

plt.title('Electricity Consumption by Sector (includ. losses)', fontsize=20, fontweight='bold')
plt.grid(visible=True, axis='y')

# plt.xlim(2013, 2021)

plt.xlabel('Year', fontsize=font_size_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_size_label)
plt.ylim(0, 555)
plt.ylabel('GWh', fontsize=font_size_label, fontweight='bold')
plt.yticks(fontsize=font_size_label)

handles, labels = plt.gca().get_legend_handles_labels()
order = [5, 4, 3, 2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order], fontsize=13.5)

print()

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
plt.savefig(f'{path_savefig}/Figure11_ElecConsoLosses.png', transparent=False, dpi=300)
# plt.show()
