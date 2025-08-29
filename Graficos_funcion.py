import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**2+5*x+6



x=np.linspace(-8,6,400)
y=f1(x)

plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.plot(x,y)
plt.show()