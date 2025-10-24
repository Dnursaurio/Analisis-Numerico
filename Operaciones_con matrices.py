import numpy as np

n = 4

Arr = np.zeros((n,n))

for i in range(n):
    for j in range (n):
        if i < j:
            Arr[i,j] = (i + 1) + (j + 1)
        elif i == j:
            Arr[i,j] = (-2) * (i+1) * (j+1)
        else:
            Arr[i,j] = 4*(i+1) + (j+1)

print("Matriz original:")
print(Arr)

# Ordenar los elementos de menor a mayor
Arr_ordenada = np.sort(Arr.flatten()).reshape(Arr.shape)

print("\nMatriz con elementos ordenados de menor a mayor:")
print(Arr_ordenada)