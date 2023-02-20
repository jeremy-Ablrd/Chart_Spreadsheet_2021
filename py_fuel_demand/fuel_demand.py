import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/" \
       "Spreadsheet for the preparation of Energy Reports ver-13.xlsx"

file = pd.read_excel(path, sheet_name="Growth 2010-2021", header=118, index_col=1)


# Power station: 141, 142, 144 (MT)
# Transport: 149, 150, 167, 171 (MT)
# Residential: 179, 180 (TOE)
# Service: 212, 213, 215 (TOE)
# Industrial: 196, 197, 198 (MT)

def make_dataframe(key, list_line):
    data_frame = pd.DataFrame([])
    if key == 'Agriculture':
        df = file.iloc[list_line:list_line + 1, 2:14].T
        data_frame = pd.concat([data_frame, df], axis=1)
        data_frame = data_frame
        data_frame.rename(columns={'Sub-total': 'Gasoil'}, inplace=True)
        return key, data_frame

    for values in list_line:
        df = file.iloc[values:values + 1, 2:14].T
        data_frame = pd.concat([data_frame, df], axis=1)
        if key == 'Transport':
            data_frame.rename(columns={'Domestic Air Jet A-1': 'Jet A-1 used by Air Transport',
                                       'Passenger & Freight Gasoil': 'Gasoil used by Marine Transport'}, inplace=True)
    print(data_frame)
    return key, data_frame


def make_stackplot(dataframe, col):
    fig, ax = plt.subplots(figsize=(12, 9))
    data_stack = []
    data_label = []
    for data in dataframe:
        list_data = dataframe[data].tolist()
        data_stack.append(list_data)
        data_label.append(data)
    print(data_stack)
    ax.stackplot(dataframe.index.tolist(), data_stack, labels=data_label, colors=col)


dict_line = {'Power Generation': ([21, 22, 24], ['#573F06', '#704E5D', '#00A3A4']),
             'Transport': ([29, 30, 51, 47], ['#704E5D', '#656543', '#164C5F',  '#312E5F']),
             'Residential': ([59, 60], ['#AC9C61', '#EA8555']),
             'Service': ([92, 93, 95], ['#AC9C61', '#704E5D', '#EA8555']),
             'Industrial': ([77, 78, 76], ['#573F06', '#704E5D', '#AC9C61']),
             'Agriculture': (109, '#704E5D'),
             }

font_label = 16
for i in dict_line:
    name, new_dataframe = make_dataframe(i, dict_line[f'{i}'][0])
    colors = dict_line[f'{name}'][1]

    sns.set(style='white')

    make_stackplot(new_dataframe, colors)
    # ----- Another way to make Area chart ----- #
    # new_dataframe.plot(kind='area', y=[f'{columns}' for columns in new_dataframe.columns], figsize=(12, 9),
    #                         color=colors)

    plt.title(f"{name} Sector", fontsize=21, fontweight='bold')
    plt.xlabel('Year', fontsize=font_label, fontweight='bold')
    plt.xlim(2010, 2021)
    plt.xticks(fontsize=font_label)
    plt.yticks(fontsize=font_label)

    if name == 'Residential' or name == 'Service':
        plt.ylabel('TOE', fontsize=font_label, fontweight='bold')
    else:
        plt.ylabel('Metric Ton', fontsize=font_label, fontweight='bold')

    handles, labels = plt.gca().get_legend_handles_labels()
    order = [i for i in reversed(range(len(new_dataframe.columns)))]
    plt.legend([handles[i] for i in order], [labels[i] for i in order], loc='upper left', fontsize=12)

    path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
    plt.savefig(f'{path_savefig}/figure_Fuel_Demand_{name}.png', transparent=False, dpi=300)


plt.show()
