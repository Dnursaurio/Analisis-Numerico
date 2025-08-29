import numpy as np

def f(x):
    return np.exp(x)-np.log(x+1)*np.cos(x)-2

x=-5
for i in range(50):
    x1 = x + 0.5 * i
    x2 = x1 + 0.5
    P = f(x1)*f(x2)
    print(f'[{x1};{x2}] tiene un valor de P= {P}')
