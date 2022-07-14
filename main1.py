import base64
from io import BytesIO

from scipy.interpolate import griddata
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from matplotlib import cm
import data


class InterpApp:
    def __init__(self, method: str, lines: int, url: str):
        self.url = url
        self.lines = lines
        self._takeData()
        self.interp(method)

    def _takeData(self):
        eData = data.DataExcel(self.url)
        eData._loadData()
        self.x = eData.x
        self.y = eData.y
        self.z = eData.z

    def interp(self, method):
        yi = np.linspace(min(self.y), max(self.y), 1000)
        xi = np.linspace(min(self.x), max(self.x), 1000)

        self.X, self.Y = np.meshgrid(xi, yi)

        self.Z = griddata((self.x, self.y), self.z, (self.X, self.Y), method=method)

    def printPlot(self):
        lvl = np.linspace(np.min(self.z), np.max(self.z), self.lines)
        lvl2 = [lvl[i] for i in range(5, len(lvl), round(self.lines * 0.2))]
        fig = Figure()
        ax = fig.subplots()

        ls = LightSource(275, 45)
        rgb = ls.shade(self.Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')

        ax.contourf(self.X, self.Y, self.Z, lvl, facecolors=rgb, shade=False)
        ax.contour(self.X, self.Y, self.Z, lvl, colors='black', extend='both', linewidths=.5)

        cntr2 = ax.contour(self.X, self.Y, self.Z, lvl2, colors='black', extend='both')

        ax.clabel(cntr2, levels=lvl2, fmt="%4i", fontsize='14', use_clabeltext=True)
        ax.set_title('Сплайн интерполяция кровли пласта')
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return f"<img src='data:image/png;base64,{data}'/>"
        # plt.show()
