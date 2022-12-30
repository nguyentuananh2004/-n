def cau1():
  from ast import increment_lineno
  import numpy as np
  import matplotlib.pyplot as plt
  from matplotlib import cm
  def ham_yen_ngua(a, x, y):
    z = (x/3)**2 - (y/2)**2
    return z
  x = np.linspace(start=-5, stop=5,num=200)
  y = np.linspace(start=-5, stop=5,num=200)
  x, y = np.meshgrid(x, y)
  z = ham_yen_ngua(0, x, y)
  fig, ax =plt.subplots(subplot_kw={"projection":"3d"})
  rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
  ax.set_zlim(-5, 3)
  fig.colorbar(rosen_surf, shrink=0.5,aspect=5)
  plt.show()


cau1()