import numpy as np

n = 4

Arr = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i<j:
            Arr[i,j] = np.abs((i+1)-(j+1))
        else:
            Arr[i,j] = (i+1)+(j+1)

Brr = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i < j:
            Brr[i,j] = (j + 1)**(i+1)
        else:
            Brr[i,j] = (i + 1) * (j + 1)

print("Matriz Arr")
print(Arr)
print("Matriz Brr")
print(Brr)
print("Operacion X")