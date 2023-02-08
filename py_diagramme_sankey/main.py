# -------- IMPORT -------- #
import json
from data_input import *

page = True
print("------------------ File main.py ------------------")


# ---- MAIN ---- #
def main_code(dict_data, list_data,):
    src = []
    targ = []
    lbl_in_dict = []
    val = []
    for list_d in list_data:
        index, section = list_d

        if section in dict_data.keys():
            lbl_in_dict.append(section)
            print(f"------ {section.upper()} ------")

            # --- CONDITION REMOVE NONE --- #
            if None in dict_data[f'{section}']:
                nb_element_in_dict = len(dict_data[f'{section}']) - 1
            else:
                nb_element_in_dict = len(dict_data[f'{section}'])

            list_source = create_source(nb_element_in_dict, index)
            list_target = create_target(dict_data[f'{section}'], list_data)
            list_value = create_value(dict_data[f'{section}'])
            src.extend(list_source)
            targ.extend(list_target)
            val.extend(list_value)
            print()

    print('----------- Data Final -------------')
    # -- Managed ERROR --- #
    if not len(lbl_in_dict) == len(dict_data):
        print(f"WARNING ! Elements of list and dictionary don't match ! length of label({len(lbl_in_dict)}) "
              f"and dict({len(dict_data)}) must be the same.")
        return None, None, None

    elif not len(src) == len(targ):
        print(f"WARNING ! Something is wrong ! length of source({len(src)}) "
              f"and target({len(targ)}) must be the same.")
        return None, None, None
    # -------------------- #

    else:
        print("LABEL in dictionary", lbl_in_dict)
        print("SOURCE", src)
        print("TARGET", targ)
        print("VALUE", val)
        return src, targ, val


# OTHER FUNCTION  #
def create_source(length_element, index_list):
    list_s = []
    while length_element > 0:
        list_s.append(index_list)
        length_element += -1
    print("list SOURCE :", list_s, f"({len(list_s)})")
    return list_s


def create_target(values_in_dict, list_keywords):
    index_values = 0
    list_t = []
    while index_values < len(values_in_dict):
        for tup in list_keywords:
            if values_in_dict[index_values][0] == tup[1]:
                list_t.append(tup[0])
                break
        index_values += 1
    print("list TARGET", list_t, f"({len(list_t)})")
    return list_t


def create_value(values_in_dict):
    list_v = []
    for tup_1 in values_in_dict:
        list_v.append(tup_1[1])
    print("list VALUE", list_v, f"({len(list_v)})")
    return list_v


# ---- IMPORT DATA from data_input.py ---- #
label = []
for i in list_label:
    label.append(i[1])
print("All label :", label)

source, target, value = main_code(dict_link, list_label)
data = {
    "node": {
        "label": label,
        "color": color_node,
    },
    "link": {
        "source": source,
        "target": target,
        "value": value,
        "color": color_link,
        "label": [],
    }
}

# --------  SERIALIZE DATA in JSON format -------- #

if color_node and color_link:

    path = "C:/Users/jerem/Desktop/Chart_Spreadsheet_2021/py_diagramme_sankey"
    f = open("data_output.json", 'r')
    data_json = f.read()
    f.close()

    data_read = json.loads(data_json)

    # add element in data_output.json
    data_read['data'][0]['node']['label'] = data['node']['label']
    data_read['data'][0]['node']['color'] = data['node']['color']
    data_read['data'][0]['link']['source'] = data['link']['source']
    data_read['data'][0]['link']['target'] = data['link']['target']
    data_read['data'][0]['link']['value'] = data['link']['value']
    data_read['data'][0]['link']['color'] = data['link']['color']

    f_input = open(f"{path}/data_output.json", "w")
    f_input.write(json.dumps(data_read, indent=2))
    f_input.close()

else:
    print("----------")
    print("ERROR on data_input.py !")
    print("----------")
    page = False



