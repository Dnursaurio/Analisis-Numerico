# Analisis-Numerico

primero importamos la libreria numpy
import numpy as np

"Potenciacion"
- Para poder hacer potenciacion:
    - np.power(base,exponente)
- normalmente en python es:
    - base**exponente

"Raiz"
- en numpy seria:
    - np.sqrt(x) [equivalente a la raiz cuadrada de toda la vida]
- raiz cubica:
    - np.cbrt(x)
- raiz n:
x**(1/n) n es el indice de la raiz

"Contantes principales en numpy"
- np.pi: devuelve el valor de pi (3.14159...)
- np.e: devuekve el valor de e (2.71828...)
- np.inf: valores infinutos positivos
- -np.inf: valores infinitos negativos

"Funciones trigronometricas en numpy"
- np.sin(x): seno de x (en radianes)
- np.cos(x): coseno de x (en radianes)
- np.tan(x): tangente de x (en radianes)

OJO: en nmupy no existe contangente, secante, cosecante
en ese caso usar:
- 1/np.tan(x) [contangente]
- 1/np.cos(x) [secante]
- 1/np.sen(x) [cosecante] 

"Conversion entre grados y radianes"
- np.radians(grados): convierte grados a radianes
- no.degrees(radianes): convierte radianes a grados

"Funciones logaritmos en numpy"
- np.log(x): logaritmo natural de base e
- np.log2(x): logaritmo en base 2
- np.log10(x): logaritmo en base 10
- np.log(x)/np.log(b): logaritmo en cualquier base b

"Exponenciales"
- np.exp(x) -> calcula un e a la x (es como decir np.power(np.e,exponente))

"Listas en python"
- ejemplo:
    - a=[1,2,3]
    - b=[2,4,6]
    - c=[x+y for x.y in zip(a,b)]
    OJO:
    La función zip() en Python se usa para combinar elementos de dos o más iterables 
    (como listas o tuplas) en un único iterable de tuplas, emparejando los elementos en la misma posición.

"Valor absoluto"
- np.abs(x): valor absoluto de x