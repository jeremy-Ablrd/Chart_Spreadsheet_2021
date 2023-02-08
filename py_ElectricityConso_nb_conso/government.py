import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def df_database(sector, df_nb, df_e):
    # convert pandas Series to pandas Dataframe (DOMESTIC SERIES)
    new_df_nb_conso = pd.DataFrame([df_nb[f'{sector}']]).T  # "T"ransposition to columns dataframe and no rows
    new_df_nb_conso.rename(columns={f'{sector}': 'Number of consumers'}, inplace=True)
    new_df_nb_conso.index = [i for i in range(2010, 2022)]

    new_df_elec_conso = pd.DataFrame([df_e[f'{sector}']]).T
    new_df_elec_conso.rename(columns={f'{sector}': 'Consumption'}, inplace=True)

    # Obligation for the second dataframe to reset its indexes.
    new_df_elec_conso.reset_index(inplace=True, drop=True)

    print(f'{sector} Dataframe')
    print(new_df_nb_conso)  # Bar Chart
    print(new_df_elec_conso)  # line Chart

    return new_df_nb_conso, new_df_elec_conso


def generate_fig_plot(sector_lim, df_nb, df_e, font, color_list):
    sector = sector_lim[0]
    limite_y = sector_lim[1]

    sns.set(style='white')

    plt.figure(figsize=(12, 9))
    plt.grid(axis='y', visible=True)
    # only take the series of the Dataframe, in this way give you only 1 figure
    ax_nb_consumer = df_nb['Number of consumers'].plot(kind='bar', color=color_list[0], fontsize=font)
    plt.yticks(fontsize=font)

    for i, container in enumerate(ax_nb_consumer.containers):
        cont_int = np.round(container.datavalues, 1)
        ax_nb_consumer.bar_label(container, labels=cont_int, color='black',
                                 label_type='center', padding=0, fontsize=16, fontweight='bold')

    ax_elect_conso = df_e['Consumption'].plot(kind='line', secondary_y=True, color=color_list[1],)

    # ------ Config Axis ------ #
    ax_nb_consumer.set_xlabel('Year', fontsize=font, fontweight='bold')
    ax_nb_consumer.set_ylabel('Number of consumers', fontsize=font, fontweight='bold')
    plt.yticks(fontsize=font)

    ax_elect_conso.set_ylabel('Consumption GWh', fontsize=font, fontweight='bold')
    plt.yticks(fontsize=font)
    ax_elect_conso.set_ylim(0, limite_y)

    # ------ Config Title ------ #
    plt.title(f'{sector} Sector', fontsize=21, fontweight='bold')

    # ------ Config Legend ------ #
    handles1, labels1 = ax_elect_conso.get_legend_handles_labels()
    handles2, labels2 = ax_nb_consumer.get_legend_handles_labels()

    handles = handles1 + handles2
    labels = labels1 + labels2

    order = [1, 0]

    plt.legend([handles[i] for i in order], [labels[j] for j in order], loc='upper left')

    path_savefig = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/Correction_chart"
    plt.savefig(f'{path_savefig}/figure12_15_{sector}.png', transparent=False, dpi=300)

    plt.show()


# --- DATA SECTION --- #
path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/py_ElectricityConso_nb_conso/Data on sectorial electricity consumption.xlsx"
file_nbConsumer = pd.read_excel(path, sheet_name="Sheet0", header=2, index_col=0)
file_elect_conso = pd.read_excel(path, sheet_name="Sheet0", header=34, index_col=0)

df_nbConsumer = file_nbConsumer.iloc[10:22, 0:4]
df_elect_conso = file_elect_conso.iloc[10:22, 0:4]

# Rename Column Dataframe
df_nbConsumer.rename(columns={'Domestic': 'Residential', 'Commercial/ Industrial': 'Commercial & Industrial'}, inplace=True)
df_elect_conso.rename(columns={'Domestic': 'Residential', 'Commercial&Industrial': 'Commercial & Industrial'}, inplace=True)

# --------- Number of Consumers -------- #
text1 = ' Nb_Consumers '
print(f"{text1:-^30}")
print(df_nbConsumer)

print()
# --------- Electricity consumption -------- #
text2 = ' Elect_Conso '
print(f"{text2:-^30}")
print(df_elect_conso)

# --- VARIABLE --- #
# list_sector and y limit on the graph
list_s = [('Residential', 150, ['#4C72B0', '#000D7A']), ('Commercial & Industrial', 250, ['#DD8452', '#DD1900']),
          ('Government', 60, ['#55A868', '#066F00']), ('Street lighting', 1.50, ['#F7AD19', '#B12900'])]
font_size = 16


for list_ in list_s:
    new_df_nb, new_df_e = df_database(list_[0], df_nbConsumer, df_elect_conso)
    generate_fig_plot(list_, new_df_nb, new_df_e, font_size, list_[2])
