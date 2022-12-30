from ast import increment_lineno
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def ham_hyperbolic(x, y):
  z = 2*((x/3)**2+(y/5)**2-1)**(1/2)
  return z
def ham_hyperbolic1(x, y):
  z =-2 * ((x / 3) ** 2 + (y / 5) ** 2 - 1) ** (1 / 2)
  return z
x = np.linspace(start=-7, stop=7,num=1000)
y = np.linspace(start=-7, stop=7,num=1000)
x, y = np.meshgrid(x, y)
z = ham_hyperbolic(x, y)
z1 = ham_hyperbolic1(x,y)
fig, ax =plt.subplots(subplot_kw={"projection":"3d"})
rosen_surf1 = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
rosen_surf2 = ax.plot_surface(x, y, z1,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
fig.colorbar(rosen_surf1, shrink=0.5,aspect=5)
fig.colorbar(rosen_surf2, shrink=0.5,aspect=5)

plt.show()