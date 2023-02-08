import plotly.graph_objects as go
from main import *


def test_main_page(main_page):
    if main_page:
        f_output = open("data_output.json", 'r')
        data_output = f_output.read()
        f_output.close()
        return data_output
    else:
        print("----------")
        print("ERROR : cannot continue !")
        print("----------")


donnees_json = test_main_page(page)
data = json.loads(donnees_json)

fig = go.Figure(data=[go.Sankey(
    valueformat=".0f",
    valuesuffix="TOE",
    # Define nodes
    node=dict(
      pad=15,
      thickness=15,
      line=dict(color="black", width=0.5),
      label=data['data'][0]['node']['label'],
      color=data['data'][0]['node']['color']
    ),
    # Add links
    link=dict(
      source=data['data'][0]['link']['source'],
      target=data['data'][0]['link']['target'],
      value=data['data'][0]['link']['value'],
      label=data['data'][0]['link']['label'],
      color=data['data'][0]['link']['color']
    ), orientation='h')])

fig.update_layout(title_text="Seychelles Energy Balance for 2021 (Unit = TOE)",
                  font_size=19, title_font_family="Arial", title_font_size=22)
fig.show()
