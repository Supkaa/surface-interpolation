from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from matplotlib import cm
import data


class InterpApp:
    def __init__(self, method: str, lines: int):
        self._takeData()
        self.interp(method)
        self.printPlot(lines)

    def _takeData(self):
        eData = data.DataExcel
        eData._loadData(eData)
        self.x = eData.x
        self.y = eData.y
        self.z = eData.z

    def interp(self, method):
        yi=np.linspace(min(self.y), max(self.y), 1000)
        xi=np.linspace(min(self.x), max(self.x), 1000)

        self.X, self.Y= np.meshgrid(xi,yi)

        self.Z = griddata((self.x, self.y), self.z, (self.X, self.Y), method=method)

    def printPlot(self, lines: int):
        lvl = np.linspace(np.min(self.z), np.max(self.z), lines)
        lvl2 = [lvl[i] for i in range(5, len(lvl), round(lines*0.2))]

        fig, ax = plt.subplots()

        ls = LightSource(275, 45)
        rgb = ls.shade(self.Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')

        cs = ax.contourf(self.X, self.Y, self.Z, lvl, facecolors=rgb, shade=False)
        cntr1 = ax.contour(self.X, self.Y, self.Z, lvl, colors='black', extend='both', linewidths=.5)

        cntr2 = ax.contour(self.X, self.Y, self.Z, lvl2, colors='black', extend='both')

        ax.clabel(cntr2, levels=lvl2, fmt="%4i", fontsize='14',use_clabeltext=True)
        ax.set_title('Сплайн интерполяция кровли пласта')


        fig.savefig('dd.pdf')
        plt.show()


if __name__ == '__main__':
    app = InterpApp('cubic', 30)

