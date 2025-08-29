import numpy as np
import matplotlib.pyplot as plt

def f_tramo1(x):
    return 5*np.cos(x**2-x)

def f_tramo2(x):
    return x**2+3*x+5

def f(x):
    return np.piecewise(x,[(x<0),(x>0)],[f_tramo1,f_tramo2])

x= np.linspace(-4,4,400)
y=f(x)


plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.plot(x,y)
plt.show()
