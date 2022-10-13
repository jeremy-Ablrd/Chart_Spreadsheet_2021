import matplotlib.pyplot as plt

# ------- Function Generate Figure ------- #


class Chart:
    def __init__(self, x, y, z):
        self.ax = plt.subplot(x, y, z)  # left (1, 2, 1) or right (1, 2, 2)

    def pie_chart(self, x, labels, colors, explode=None, label_dist=None, wedge_prop=None, text_prop=None):
        pie = self.ax.pie(x=x, labels=labels, colors=colors,
                          explode=explode,
                          labeldistance=label_dist,   # or None
                          wedgeprops=wedge_prop,
                          textprops=text_prop,
                          autopct=None,  # or None
                          shadow=False, startangle=-0, counterclock=False, frame=False,
                          # center=(1.2,1.2),
                          )
        return pie


'''
fig.add_artist(patches.Rectangle((0.57, 0.255), 0.31, 0.48,                    #Position de l'object entre parenthese, le reste sont les dimention x et y
               edgecolor = 'black', facecolor = 'orange',
               fill = False,
                alpha = 0.5,
                #hatch = '/',
                #linestyle = 'dashed',
                linewidth = 1, zorder = 1))

fig.add_artist(patches.Rectangle((0.44, 0.498), 0.132, 0,                    #Position de l'object entre parenthese, le reste sont les dimention x et y
                edgecolor = 'black', facecolor = 'orange',
                fill = False,
                angle = -5.5,
                alpha= 0.6,
                #hatch = '/',
                #linestyle = 'dashed',
                linewidth = 1.2, zorder = 1))

fig.add_artist(patches.Rectangle((0.44, 0.498), 0.132, 0,                    #Position de l'object entre parenthese, le reste sont les dimention x et y
                edgecolor = 'black', facecolor = 'orange',
                fill = False,
                angle = 5.5,
                alpha=0.6,
                #hatch = '/',
                #linestyle = 'dashed',
                linewidth = 1.2, zorder = 1))

#plt.title('Store Inventory')
#plt.ylabel('Product')
#plt.xlabel('Quantity')

 ########       SAVE FIGURE     ##########
plt.savefig('AllFuel2020.png', transparent=True, dpi=300)
plt.show()'''
