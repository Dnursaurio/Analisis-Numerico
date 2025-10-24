import numpy as np

def f(x):
  if x<=20 and x>=2:
    return np.exp(x) - np.log(x + 1) * np.cos(x - 2)

x=2
print("los intervalos con raices reales son:")
for i in range(45):
  x1 = x + 0.5 * i
  x2 = x1 + 0.3
  P = f(x1)*f(x2)
  print(f'[{x1};{x2}] tiene un valor de P= {P}')