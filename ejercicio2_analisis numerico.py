import numpy as np
m=np.array([1/3,2/5,3/7])
n=np.radians(np.array([35,50,65]))
o=np.array([2,4,6])

primera_parte = (np.power((m/np.sin(2*n-3))-o,2) + np.cos(3*n + 2))
segunda_parte = (np.sqrt(np.power(np.log(o+np.power(m,-3)),3))+ m/o+1)

print(primera_parte/segunda_parte)