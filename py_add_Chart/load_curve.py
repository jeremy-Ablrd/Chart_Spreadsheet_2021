# import numpy
# import matplotlib.ticker as mtick
import matplotlib.dates as md

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Load curves for Mahe and Praslin for the days with Maximum Peak Demand.xlsx"
file_mahe = pd.read_excel(path, sheet_name="Sheet1", header=1, index_col='Time', parse_dates=True, )
file_praslin = pd.read_excel(path, sheet_name="Sheet1", header=2, index_col='Time', parse_dates=True, )


def make_chart(df_list):
    df_name = df_list[0]
    df_island = df_list[1]
    df_date = df_list[2]
    df_ylim = df_list[3]
    df_color = df_list[4]
    sns.set(style='white')
    fig, ax = plt.subplots(figsize=(12, 9))

    ax.plot(df_island.index, df_island['Power Demand'], color=df_color, marker='o')

    ax.xaxis.set_major_locator(md.MinuteLocator(byminute=[0, 0]))
    ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)

    font_label = {'size': 17, 'weight': 'bold'}
    font_value = 14
    plt.title(f'Load curve for {df_name} on {df_date}', fontdict={'size': 22, 'weight': 'bold'})

    plt.grid(axis='x', visible=True)

    offset = 0.2
    v_index = 0
    for row in df_island['Power Demand']:
        if row == df_island['Power Demand'].max():
            ax.annotate(f"{round(df_island['Power Demand'].max())} MW", color='#B12900',
                        xy=(df_island.index[v_index], df_island['Power Demand'].max() + offset),
                        verticalalignment='bottom', horizontalalignment='left', fontsize=18, fontweight='bold')
        v_index += 1

    plt.xlabel('Time', fontdict=font_label)
    plt.xticks(fontsize=font_value)
    plt.ylabel('Power demand (MW)', fontdict=font_label)
    plt.yticks(fontsize=font_value)
    plt.ylim(0, df_ylim)

    path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart_Energy_Report"
    plt.savefig(f'{path_savefig}/Figure10-11_Load_curve_{df_name}.png', transparent=False, dpi=300)

    plt.show()


df_mahe = file_mahe.iloc[2:24, 2:3]
df_mahe = df_mahe / 1000
print(df_mahe)

df_praslin = file_praslin.iloc[1:24, 12:14]
df_praslin = df_praslin / 1000
print(df_praslin)

df_list_comp = [('Mahe', df_mahe, 'Wednesday 19th May 2021', 70, '#0700CC'),
                ('Praslin', df_praslin, 'Tuesday 16th November 2021', 10, '#00A805')]

for data_frame in df_list_comp:
    make_chart(data_frame)
