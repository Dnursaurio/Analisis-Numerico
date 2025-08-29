import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.e**x-np.log(x+1)*np.cos(x)-2

x= np.linspace(-2,2,400)
y=f(x)


plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.plot(x,y)
plt.show()
