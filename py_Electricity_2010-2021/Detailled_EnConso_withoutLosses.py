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

new_df = pd.concat([df_indus_commerce, df_residential, df_government, df_street], axis=1)
for columns in new_df.columns:
    new_df[f'{columns}'] = [round(i, 2) for i in new_df[f'{columns}']]

print(new_df)


sns.set(style='white')
colors = ['#DD8452', '#4C72B0', '#55A868', '#F7AD19']
ax = new_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 9))

label_color = ['black' for i in range(len(new_df))]

font_size_values = 18

for i, container in enumerate(ax.containers[:3]):
    cont_int = np.round(container.datavalues, 1)
    ax.bar_label(container, labels=cont_int, color=label_color[i],
                 label_type='center', padding=0, fontsize=font_size_values, fontweight='bold')

for i, container_street_light in enumerate(ax.containers[3:]):
    cont_int = np.round(container_street_light.datavalues, 1)
    ax.bar_label(container_street_light, labels=cont_int,
                 color=label_color[i], label_type='edge', padding=0,
                 fontsize=font_size_values, fontweight='bold')

plt.title('Electricity Consumption by Sector', fontsize=21, fontweight='bold')
plt.grid(visible=True, axis='y')

font_size_label = 18

plt.xlabel('Year', fontsize=font_size_label, fontweight='bold')
plt.xticks(rotation=0, fontsize=font_size_label)
plt.ylim(0, 450)
plt.ylabel('GWh', fontsize=font_size_label, fontweight='bold')
plt.yticks(fontsize=font_size_label)


handles, labels = plt.gca().get_legend_handles_labels()
order = [3, 2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order])
print(plt.gca().get_legend_handles_labels())
path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
# plt.savefig(f'{path_savefig}/Figure16_EnConso_bySector.png', transparent=False, dpi=300)
# plt.show()
