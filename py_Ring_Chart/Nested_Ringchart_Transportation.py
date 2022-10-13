import pandas as pd
import matplotlib.pyplot as plt

path = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=99)
color = ['#6E6E71', '#018080', '#2b489d']

df = file.iloc[1:4, 0:2]
df['Gasoil'] = [11470.4, 2306.0, 0]
df['Gasoline'] = [21143.0, 1046.5, 0]
df['Jet-A1'] = [0, 0, 1869.9]
df['Avgas'] = [0, 0, 94.0]
print(df)

plt.figure(figsize=(16, 9))

plt.pie(x=df['TOE'], labels=df['SECTOR'], labeldistance=1.1, colors=color, radius=1, center=(0, 0), autopct='%2.0f%%',
        pctdistance=0.85,
        wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
        textprops={'fontsize': 22, 'color': 'black'})

circle = plt.Circle((0, 0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.axis('equal')

# path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Figure/Ring_Chart_figure_Sectorial"
# plt.savefig(f'{path_savefig}/Ringchart_Transportation_2021.png', transparent=True, dpi=300)
#
# plt.show()

"""plt.figure(figsize=(9, 6))
plt.pie(x=df['TOE'], labels=df['SECTOR'], center=(0, 0), radius=1)
plt.pie(x=df['Gasoil'], labels=df['SECTOR'], center=(0, 0), radius=0.7)
plt.show()"""

"""Road_gas = {'Gasoil': , "Gasoline": }
Maritime_gas = {'Gasoil': , "Gasoline": }
Air_gas = {'Jet-A1': , "Avgas": }"""