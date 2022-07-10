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
Z = griddata((x, y), z, (X, Y),method='cubic')

fig, ax = plt.subplots()

ls = LightSource(270, 45)
rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')

cs = ax.contourf(X, Y, Z, facecolors=rgb, shade=False)
cntr = ax.contour(X, Y, Z,
                  colors='black', extend='both')
ax.clabel(cntr, fmt="%4.1f", fontsize='7.5',use_clabeltext=True)
ax.set_title('Сплайн интерполяция кровли пласта')


fig.savefig('dd.pdf')
plt.show()