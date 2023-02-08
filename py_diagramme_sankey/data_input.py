

def list_node(liste_color):
    color_n = []
    for list_ in liste_color:
        if len(liste_color) == 20:
            color_n.append(f"rgba({list_[0]}, {opacity_node})")
        else:
            print("----------")
            print("ERROR : too little or too much element in list")
            print("----------")
            break
    return color_n


def list_link(list_color):
    global electricity
    global ener_loss
    list_l = []
    for list_ in list_color:
        nb_loop = list_[1]
        while nb_loop > 0:
            if not list_[0] == "190, 106, 73":
                list_l.append(f"rgba({list_[0]}, {opacity_link})")
            if list_[0] == "205, 78, 20":
                list_l.append(f"rgba({ener_loss[0]}, {opacity_link})")
                nb_loop -= 1
            elif list_[0] == "190, 106, 73":
                list_l.append(f"rgba({electricity[0]}, {opacity_link})")
                list_l.append(f"rgba({ener_loss[0]}, {opacity_link})")
                nb_loop -= 2
            nb_loop -= 1
    return list_l


# -------------- DATA -------------- #

list_label = [
    (0, "Fuel Oil"),
    (1, "Gasoil"),
    (2, "Gasoline"),
    (3, "LPG"),
    (4, "Jet A1"),
    (5, "PUC Power Stations"),
    (6, "Auto-Producers"),
    (7, "Agriculture & Fishing"),
    (8, "Marine Transportation"),
    (9, "Road Transportation"),
    (10, "International Marine Bunker"),
    (11, "Service"), (12, "Residential"),
    (13, "Domestic Air Transportation"),
    (14, "Electricity Grid"),
    (15, "Industry"),
    (16, "Wind"),
    (17, "Solar PV"),
    (18, "Energy Losses"),
    (19, "International Air Bunker")
]

dict_link = {
    "Fuel Oil": [
        ("PUC Power Stations", 78852), ("Industry", 4275.2), ("International Marine Bunker", 5033.3),
    ],

    "Gasoil": [
        ("PUC Power Stations", 10861,), ("Auto-Producers", 16317.7), ("Service", 3691.8), ("Industry", 2560.7),
        ("Road Transportation", 11470.4), ("Marine Transportation", 2306), ("Agriculture & Fishing", 2194.9),
        ("International Marine Bunker", 168765.7),
    ],

    "Gasoline": [
        ("Service", 455.3), ("Industry", 23.7), ("Road Transportation", 21143),
        ("Marine Transportation", 1046.5,),
    ],

    "LPG": [
        ("Residential", 3946), ("Service", 1107.2), ("Industry", 288.4)
    ],

    "Jet A1": [
        ("Domestic Air Transportation", 1869.9), ("International Air Bunker", 24673.9),
    ],

    "Electricity Grid": [
        ("Residential", 11932.1), ("Service", 22840.5), ("Industry", 5432.2)
    ],

    "Wind": [
        ("Electricity Grid", 436.8),
    ],

    "Solar PV": [
        ("Electricity Grid", 622),
    ],

    "PUC Power Stations": [
        ("Electricity Grid", 36474.2), ("Energy Losses", 78852+10861-36474.2),
    ],

    "Auto-Producers": [
        ("Auto-Producers", 5662.3), ("Energy Losses", 16317.7+5662.3-5662.3)
    ],

}

# -------------- COLOR -------------- #
opacity_node = 1
opacity_link = 0.7

# color RGB
fuel_oil = ("58, 57, 56", 3)
gasoil = ("95, 43, 28", 8)
gasoline = ("169, 0, 130", 4)
LPG = ("16, 59, 110", 3)
Jet_A1 = ("70, 33, 43", 2)
PUC_station = ("205, 78, 20", 2)
auto_prod = ("190, 106, 73", 2)
agri_fish = ("8, 117, 169", 0)
marine_transp = ("8, 117, 169", 0)
road_transp = ("8, 117, 169", 0)
marine_bunker = ("4, 4, 4", 0)
service = ("8, 117, 169", 0)
residential = ("8, 117, 169", 0)
domestic_air = ("8, 117, 169", 0)
electricity = ("168, 165, 2", 3)
industry = ("8, 117, 169", 0)
wind = ("62, 124, 59", 1)
solar_pv = ("62, 124, 59", 1)
ener_loss = ("184, 55, 40", 0)
air_bunker = ("4, 4, 4", 0)

list_rgb = [fuel_oil, gasoil, gasoline, LPG, Jet_A1, PUC_station, auto_prod, agri_fish, marine_transp, road_transp,
            marine_bunker, service, residential, domestic_air, electricity, industry, wind, solar_pv, ener_loss,
            air_bunker]
print(len(list_rgb))

color_node = list_node(list_rgb)
color_link = list_link(list_rgb)
print(color_link)
