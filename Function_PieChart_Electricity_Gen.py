import matplotlib.pyplot as plt


# Create function plt.
def figure(length, width):
    plt.figure(figsize=(length, width))


def pie_chart(x, labels, colors, explode=None, label_dist=None, wedge_prop=None, text_prop=None, auto_nb=None):
    plt.axis([0, 2.4, 0, 2.4])
    plt.pie(x=x, labels=labels, colors=colors, explode=explode, labeldistance=label_dist,
            wedgeprops=wedge_prop,
            textprops=text_prop,
            autopct=auto_nb, shadow=False, startangle=-0, counterclock=False, frame=False,
            center=(0, 0), radius=1)


def print_text(x: float, y: float, txt: str, fontsize: int, color: str, verti_align: str, horiz_align: str, bbox=None):
    plt.text(x, y, txt, fontsize=fontsize, color=color, verticalalignment=verti_align,
             horizontalalignment=horiz_align,)

