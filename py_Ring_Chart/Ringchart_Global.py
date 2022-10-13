import matplotlib.pyplot as plt
import pandas as pd

# Call file
# from file create DataFrame "df"
# make different data for "residential", "service", ect...
# create function for figure and ring chart
# build different figure for each sector (by call function)
# put in collection, make sure to factorize the programme.
# plt.show() at the end

# Call file
from pandas import DataFrame

path = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=2, index_col=0)

# Set file and pre-treatment of Dataframe, create data frame.
df = file.iloc[25:36, 0:13]
rename_columns = df.rename(columns={'Prod. (+)                 Cons. (-)': 'Electricity',
                                    'Prod. (+)                 Cons. (-).1': 'Solar Water Heater'}, inplace=True)


# ----------------- ALL FUNCTION ----------------- #

def create_data_sector(dataframe: DataFrame, sectors: list):
    # Drop NaN rows and take only values
    index_series = []
    list_series = []
    for sector in sectors:
        series = dataframe.loc[sector].dropna(axis=0)      # delete value NaN
        index_ = [index for index in series.index]
        list_ = [values for values in series]
        index_series.append(index_)
        list_series.append(value_percent(list_))
    return index_series, list_series


def value_percent(shares: list):
    share_percent = []
    for each_share in shares:
        operation = (each_share / sum(shares)) * 100
        share_percent.append(round(operation, 2))
    return share_percent


def simplified_dataframe(dataframe: DataFrame):
    dict_kfs = {}
    dict_gas = {}
    for i in dataframe.index:
        if i == "Gasoil":
            dict_gas[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)
        elif i == "Gasoline":
            dict_gas[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)
        if i == "Solar Water Heater":
            dict_kfs[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)
        elif i == "Fuelwood & charcoal":
            dict_kfs[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)
        elif i == "Kerosene":
            dict_kfs[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)

    if dict_gas:
        # ------- Sum of Gasoil and Gasoline ------- #
        dict_df1 = pd.DataFrame(dict_gas).T
        somme_gas = dict_df1.iloc[:].sum(axis=0)
        # make somme to a Series :
        somme_gas = pd.DataFrame(somme_gas, columns=['Gasoil & Gasoline']).T
        df_gas = pd.concat([dataframe, somme_gas], join='inner')
        return df_gas
    # ------- Sum of solar, fuelwood, Kerosene ------- #
    dict_df2 = pd.DataFrame(dict_kfs).T
    somme_kfs = dict_df2.iloc[:].sum(axis=0)
    # make somme to a Series :
    somme_kfs = pd.DataFrame(somme_kfs, columns=['Solar Hot Water, \nKerosene, \nCharcoal & Woodfuel']).T
    df_kfs = pd.concat([dataframe, somme_kfs], join='inner')
    return df_kfs


def assign_color(dataframe: DataFrame):
    color = []
    for i in dataframe.index:
        if i == "Electricity":
            assign = '#F1C40F'
            color.append(assign)
        elif i == "LPG":
            assign = '#A3B825'
            color.append(assign)
        elif i == "Solar Hot Water, \nKerosene, \nCharcoal & Woodfuel":
            assign = '#5499C7'
            color.append(assign)
        elif i == "Gasoil & Gasoline":
            assign = '#CD6155'
            color.append(assign)
        elif i == "Fuel Oil":
            assign = '#52BE80'
            color.append(assign)
    print("Colors :", color)
    return color


def chart(value, index, color=None):
    plt.figure(figsize=(16, 9))
    plt.pie(x=value, labels=index, colors=color, labeldistance=1.15,
            # explode=explode2,
            pctdistance=0.85,
            autopct='%2.0f%%', shadow=False, startangle=-0, counterclock=False, frame=False,
            wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
            textprops={'fontsize': 27, 'color': 'black'}
            # center=(1.2,1.2)
            )
    circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.axis('equal')


# ----------------- CONFIG DATA for ring chart ----------------- #

SECTORS = ['Residential', 'Service', 'Industry', ]
index_global, energy_global = create_data_sector(df, SECTORS)        # call of function
path = "C:/Users/jerem/Desktop/Chart_spreadsheet_2021/Figure/Ring_Chart_figure_Sectorial"

# call data in for loop
for energy, label in enumerate(index_global):
    en_sector = energy_global[energy]
    n_df = pd.DataFrame(en_sector, columns=['Value'], index=label)
    simplified_df = simplified_dataframe(n_df)
    sorted_simplified_df = simplified_df.sort_values(by=['Value'], axis=0, ascending=False)
    # PRINT DATA
    print(SECTORS[energy], "Sector :")
    print(sorted_simplified_df)
    colors = assign_color(sorted_simplified_df)
    print()
    # CHART
    chart(sorted_simplified_df['Value'], sorted_simplified_df.index, colors)
    plt.savefig(f'{path}/RingChart_{SECTORS[energy]}_2021.png', transparent=True, dpi=300)

plt.show()
