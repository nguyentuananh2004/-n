import numpy as np
import random

def tinh_tich_xA():
    x = []
    A = []
    np.random.seed(123)
    x = np.random.randint(low=-3, high=3, size=4)
    print(x)
    A = np.random.randint(-10, 10, size=(4, 4))
    print(A)
    print('x*A :', x @ A)


tinh_tich_xA()



def nhan_hadamard():
    A1 = []
    B1 = []
    A1 = np.random.randint(-10, 10, size=(2, 3))
    B1 = np.random.randint(-10, 10, size=(2, 3))
    print(A1)
    print(B1)
    h = np.multiply(A1, B1)
    print('Hadamard product = ', h)


nhan_hadamard()


def nhan_AT_B():
    _a = [[2, 8, -8], [-6, -7, 1]]
    A1 = np.array(_a)
    _b = [[-9, 0, 6], [-3, -1, -3]]
    B1 = np.array(_b)
    a = np.array(A1)
    print(a.T)
    print('a*B1 :', a * B1)


nhan_AT_B()




def main():
    tinh_tich_xA()
    nhan_hadamard()
    nhan_AT_B()


if __name__ == "__main__":
    main()

#cau2


def he_phuong_trinh():
    from sympy import symbols, Eq, solve
    x, y, z = symbols('x y z')
    eq1 = Eq(2 * x - 5 * y + z + 5, 0)
    eq2 = Eq(4 * x + 2 * y - 2 * z - 2, 0)
    eq3 = Eq(x + y - z, 0)
    answer = solve((eq1, eq2, eq3), (x, y, z))
    print(answer)
he_phuong_trinh()



from sympy import *
def gioi_han():
    x = symbols('x')
    f = (x ** 3 - 3 * x ** 2) ** 1 / 3 + (x ** 2 - 2 * x) ** 1 / 2
    answer = limit(f, x, oo)
    print('Kết quả giới hạn: ', answer)
gioi_han()




def dao_ham():
    x = symbols('x')
    f = (2 * x - 1) / (x + 2)
    answer = diff(f, x)
    print(answer)
dao_ham()




def nguyen_ham():
    x = symbols('x')
    f = x / x ** 2 + 1
    answer = integrate(f, x)
    print(answer)
nguyen_ham()



from sympy import *
def tich_phan():
    x = symbols('x')
    f = (1 - x * tan(x)) / (x ** 2 * cos(x) + x)
    answer = integrate(f, (x, pi, 2 * pi))
    print(answer)
tich_phan()




def main():
    he_phuong_trinh()
    gioi_han()
    dao_ham()
    nguyen_ham()
    tich_phan()


if __name__ == "__main__":
    main()

#câu3


#hàm y

import numpy as np
import matplotlib.pyplot as plt


def ham_bac_4(a, b, c, x):
    f = a * x ** 4 + b * x ** 2 + c
    return f


x = np.linspace(start=-10.0, stop=10.0, num=1000)
y = ham_bac_4(1, -2, -3, x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

#hàm y'

from sympy import *

x = symbols('x')
f = x ** 4 - 2 * x ** 2 - 3
answer = diff(f, x)
print(answer)

import numpy as np
import matplotlib.pyplot as plt
def ham_bac_3(a, b, x):
    f = a * x ** 3 + b * x
    return f


x = np.linspace(start=-10.0, stop=10.0, num=1000)
y = ham_bac_3(4, -4, x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

#hàm f"

x = symbols('x')
f = 4 * x ** 3 - 4 * x
a = diff(f, x)
print(a)

import numpy as np
import matplotlib.pyplot as plt
def ham_bac_2(a, b, x):
    f = a * x ** 2 + b
    return f


x = np.linspace(start=-10.0, stop=10.0, num=1000)
y = ham_bac_2(12, -4, x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

#hàm y'''

x = symbols('x')
f = 12*x**2 - 4
a = diff(f, x)
print(a)

import numpy as np
import matplotlib.pyplot as plt
def ham_bac_1(a, x):
  f = a*x
  return f
x = np.linspace(start=-10.0,stop=10.0, num=1000)
y = ham_bac_1(24, x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()



def hinh():
  import matplotlib.pyplot as plt
  fig, ax = plt.subplots()
  x = np.linspace(start=-5.0,stop=5.0, num=1000)
  y1 = ham_bac_4(1,-2,-3, x)
  y2 = ham_bac_3(4, -4, x)
  y3 = ham_bac_2(12, -4, x)
  y4 = ham_bac_1(24, x)
  ax.plot(x, y1)
  ax.plot(x, y2)
  ax.plot(x, y3)
  ax.plot(x, y4)
  ax.set_xlabel("Trục hoành - x")
  ax.set_ylabel("Trục tung - y")
  ax.plot(x, y1, label=r'$y=ax^4+bx^2+c$')
  ax.plot(x, y2, label=r'$y=ax^3+bx$')
  ax.plot(x, y3, label=r'$y=ax^2 + b$')
  ax.plot(x, y4, label=r'$y=ax $')
  ax.set_title("Đồ thị ham bac 1, bac 2, bac 3, bac 4")
  ax.legend()
  plt.show()

hinh()

#câu 4

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




def cau2():
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

cau2()




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




def main():
  cau1()
  cau2()
  cau3()



if __name__ == "__main__":
  main()