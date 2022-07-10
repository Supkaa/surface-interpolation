from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from matplotlib import cm
import data


y = data.y
x = data.x
z = data.z

yi=np.linspace(min(y), max(y), 1000)
xi=np.linspace(min(x), max(x), 1000)

X, Y= np.meshgrid(xi,yi)
Z = griddata((x, y), z, (X, Y), method='cubic')
lvl = np.linspace(np.min(z), np.max(z), 25)
lvl2 = [lvl[i] for i in range(5, len(lvl), 5)]

fig, ax = plt.subplots()

ls = LightSource(275, 45)
rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')

cs = ax.contourf(X, Y, Z, lvl, facecolors=rgb, shade=False)
cntr1 = ax.contour(X, Y, Z, lvl, colors='gray', extend='both', linestyle='dashed', linewidths=.5)

cntr2 = ax.contour(X, Y, Z, lvl2, colors='black', extend='both')

ax.clabel(cntr2, levels=lvl2, fmt="%4i", fontsize='14',use_clabeltext=True)
ax.set_title('Сплайн интерполяция кровли пласта')


fig.savefig('dd.pdf')
plt.show()