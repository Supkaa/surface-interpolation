import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import SmoothBivariateSpline

y = np.array([5391,5396,5408,5405,4300,4312,4300,4310,5090,5100,5132,5160,5120,4580,4590,4600,4610,4590,4840,4880,4900,4870,4850,4840,5020,5460,5780,5760,4240,3915,3875,4980], dtype=float)
x = np.array([2400,2900,3470,3965,2350,2945,3550,4035,2170,2640,3220,3780,4330,2220,2640,3230,3810,4345,2430,2930,3510,4030,4530,1925,1420,1890,2670,3745,1910,2725,3770,5130], dtype=float)
z = [2850.5,2838.2,2836,2843,2849.1,2839.2,2838.2,2840.3,2839,2829,2824,2831.1,2837,2839,2832,2825,2830.1,2839,2824.1,2814,2815.1,2822,2835.2,2837.1,2857.1,2863.1,2858.3,2856.1,2862.3,2861.9,2858.2,2856.3]
zz = np.array(z, dtype=float)


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





