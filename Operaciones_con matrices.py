import numpy as np

n = 5

Arr = np.zeros((n,n))

for i in range(n):
    for j in range (n):
        if i < j:
            Arr[i,j] = (-1)**(i + 1) + (j + 1)
        elif i == j:
            Arr[i,j] = (i+1) + (j+1)
        else:
            Arr[i,j] = (-1)**(j + 1) + (i + 1)

print(Arr)