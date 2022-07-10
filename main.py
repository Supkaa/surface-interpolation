import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import SmoothBivariateSpline
import data

y = data.y
x = data.x
z = data.z
zz = np.array(z, dtype=float)


points = zip(x, y)
points = sorted(points, key=lambda point: point[0])
x, y = zip(*points)


# zi = zip(x, y)
# zis = sorted(zi, key=lambda tup: tup[0])
# print(zis)
#
# x1 = np.array([i[0] for i in zis], dtype=float)
# y1 = np.array([i[1] for i in zis], dtype=float)

xmin, xmax = min(x), max(x)
ymin, ymax = min(y), max(y)

interpol = SmoothBivariateSpline(x, y, z)

d = 0.8
x2, y2 = np.arange(xmin, xmax, d), np.arange(ymin, ymax, d)
X, Y = np.meshgrid(x2, y2)
Z = interpol.ev(X, Y)

fig, ax = plt.subplots(figsize=(30, 30))

cntr = ax.contour(X, Y, Z,
                  colors='black')
ax.clabel(cntr, fmt="%4.1f", use_clabeltext=True)

# ax.set_xlim(0, xmax)
# ax.set_ylim(0, ymax)

fig.savefig('dd.pdf')
plt.show()
