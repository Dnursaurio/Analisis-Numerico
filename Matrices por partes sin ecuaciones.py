import numpy as np

n = 5

Arr = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i<j:
            Arr[i,j] = (-1)*(i+1)*(j+1)
        else:
            Arr[i,j] = (i+1) * (j+1)

Brr = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i < j:
            Brr[i,j] = (-1)**(i + 1) + (j + 1)
        elif i == j:
            Brr[i,j] = (i+1) + (j+1)
        else:
            Brr[i,j] = (-1)**(j + 1) + (i + 1)

print("Matriz Arr")
print(Arr)
print("Matriz Brr")
print(Brr)
print("Operacion X")
X = np.linalg.inv(Arr - np.eye(n))@Brr@Arr@np.linalg.inv(Brr)
print(np.round(X,2))