def cau3():
  from ast import increment_lineno
  import numpy as np
  import matplotlib.pyplot as plt
  from matplotlib import cm
  def ham_matcau(a, x, y):
    z = np.sqrt(4-(x+2)**2-(y-1)**2)+4
    return z
  def ham_matcau1(a, x, y):
    z = -np.sqrt(4-(x+2)**2-(y-1)**2)+4
    return z
  x = np.linspace(start=-4, stop=2.5,num=1000)
  y = np.linspace(start=-4, stop=2.5,num=1000)
  x, y = np.meshgrid(x, y)
  z = ham_matcau(0, x, y)
  z1 = ham_matcau1(0, x, y)
  fig, ax =plt.subplots(subplot_kw={"projection":"3d"})
  rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
  rosen_surf1 = ax.plot_surface(x, y, z1,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)

  fig.colorbar(rosen_surf, shrink=0.5,aspect=5)
  fig.colorbar(rosen_surf1, shrink=0.5,aspect=5)
  plt.show()

cau3()