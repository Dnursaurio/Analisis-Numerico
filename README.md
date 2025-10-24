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
        - en nmupy para declarar una lista usar np.array([1,2,3]) 
        OJO:
        La función zip() en Python se usa para combinar elementos de dos o más iterables 
        (como listas o tuplas) en un único iterable de tuplas, emparejando los elementos en la misma posición.

    "Valor absoluto"
    - np.abs(x): valor absoluto de x

    "Declaracion de funciones en python"
    -   usar unicamente def (palabra clave para declarar fuciones en python):
        - seria asi:

            def "Nombre de la funcion (sin comillas ni espacios)"(parametros):
                definición de la funcion (que quieres que hga esta funcion)

    "Libreria grafica matplotlib.pyplot de python"
    -   Esta libreria puedes intalarla abriendo el cmd o un terminal en Visual Studio y copiando el siguiente comando:
        -   pip install matplotlib
    -   Luego en un nuevo scrpit de python:
        -   import matplotlib.pyplot as plt

    "Matrices con python numpy"
    -   para delcarar una matriz con numpy tenemos que declara runa array:
        -   A = np.array([1,2,3],[4,5,6])
            print("matriz A",A)
        -   para matrices con 0's usar:
            -   np.zeros((n_filas,n_columnas))
        -   matriz de unos:
            -   np.ones((n_filas,n_columnas))
        - matriz de numeros aleatorios:
            -   np.random.rand(n_filas,n_columnas)
            -   Si quieres añadirles un rango usa randint:
                -   np.random.randint(indice_inicial, indice final + 1, size=(n_filas,n_columnas))
    
#   Indexacion de matrices
    Ponte que declaramos una matriz:
-   B = np.array([[1,2,3],[4,5,6]]) <br>
    Esto genera algo asi:
-   [[1,2,3]<br>[4,5,6]]<br>
    para acceder a un elemento debemos recorda que cada elemntos del array comienza en 0
    entonces para acceder decimos:
-   print(B[0,]), esto devolveria toda la fila 0: 1,2,3
-   pero si hacemos algo asi: <br>
    print(B[0,0]), esto devuelve el primer elementos de la fila 0: 1

    "Operaciones con matrices"<br>
#   Suma de matrices
-   Del texto anterior usemos A y B:<br>
    para operar esas matrices unicamente usar <br>
    print(A+B) 
#   Producto K con una Matriz
-   Puedes hacer algo como <br>
    print(3*B)<br>
    esto te devolvera <br>
    [[3,6,9]<br>
    [12,15,18]]
    OJO: para multiplicar matrices con numpy NO usar print(A*B), esto no multiplica bien
#   Producto de matrices
-   Para hace esto correctamente unicamente usar @ en vez de * <br>
    print(A@B)
#   Transpuesta de una matriz
-   Para esto usar A.T
#   Inversa de una Matriz
-   np.linalg.inv(A)
#   Determinante de una Matriz
-   np.linalg.det(A)

Consejo <br>
-   Para reondear en numpy:
    -   Usar np.round(El numero, la cantidad de decimales a redondear)

#   Polinomios
ahora usaremos la libreria de python sympy con: <br>
from sympy import *
-   Para nombrar simbolos usar la palabra clave symbols('nombre dle simbolo')
-   Ejemplo: <br>
    from sympy import*
    x = symbols('x')
    x
-   esto devuelve x como un simbolo de ecuacion
-   Para mostrar varias ecuaciones a la vez usar display('aqui van el resto de comandos') <br>
    no basta con hacer llamadas independientes como el ejemplo anterior <br>
    ya que sympy unicamente guarda la ultima ecuacion llamada
-   OJO: puedes usar print pero esto no saldra con simbolos,<br> 
    talvez te confundas con la forma tradicional de python
-   Para expandir cualquier ecuacion usar la parabra clave expand(aqui llamas a tu variable que guarde la ecuacion)
-   Para reemplazar variables en una ecuacion usar subs(tu ecuacion, el valor de la variable)
-   Si tenemos dos ecuaciones como una P y otra Q podemos usar el comando div(P,Q) esto devolvera un par ordenado <br>
    donde la primera parte es el cocience de esa division y la segunda es el residuo de la division de esas ecuaciones
    -   Para acceder al cociente solamente usar div(P,Q)[0] y para el residuo [1]