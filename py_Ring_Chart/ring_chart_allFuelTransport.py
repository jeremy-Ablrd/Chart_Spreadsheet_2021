import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=99)

df = file.iloc[1:4, 0:1]
df['Gasoil'] = [11470.4, 2306.0, 0]
df['Gasoline'] = [21143.0, 1046.5, 0]
df['Jet-A1'] = [0, 0, 1869.9]
df['Avgas'] = [0, 0, 94.0]
print(df)

gasoil = sum(df['Gasoil'])
gasoline = sum(df['Gasoline'])
jet_a1 = sum(df['Jet-A1'])

fuel = [gasoil, gasoline, jet_a1]
fuel_share = [(f/sum(fuel))*100 for f in fuel]
title = [t for t in df.columns[1:4]]

print(fuel, title)

plt.figure(figsize=(12, 9))

color = sns.color_palette('tab10')
plt.pie(x=fuel_share, labels=title, labeldistance=1.1,
        colors=color,
        radius=1, center=(0, 0), autopct='%1.0f%%',
        pctdistance=0.85,
        wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
        textprops={'fontsize': 25, 'color': 'black'})

circle = plt.Circle((0, 0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.axis('equal')

path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Ring_Chart_figure_Sectorial"
plt.savefig(f'{path_savefig}/Ringchart_TransportationFuelType_2021.png', transparent=True, dpi=300)

plt.show()
