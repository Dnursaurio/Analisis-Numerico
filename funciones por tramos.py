import numpy as np
import matplotlib.pyplot as plt

def f_tramo1(x):
    return x**2

def f_tramo2(x):
    return np.cos(x)

def f(x):
    return np.piecewise(x,[(x>-5)&(x<5),(x>10)&(x<20)],[f_tramo1,f_tramo2])

x= np.linspace(-5,20,400)
y=f(x)

plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.plot(x,y)
plt.show()
