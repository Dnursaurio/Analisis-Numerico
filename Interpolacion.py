#manejando pilinomios en python
from sympy import*

x = symbols('x')
x
l0 = ((x-3)*(x-4))/6
l1 = ((x-1)*(x-4))/-2
l2 = ((x-1)*(x-3))/3
print("ecuaciones: L0")
display(l0)
print("ecuaciones: L1")
display(l1)
print("ecuaciones: L2")
display(l2)
print("L0 expandido")
display(expand(l0))
print("L1 expandido")
display(expand(l1))
print("L2 expandido")
display(expand(l2))
print("ahora P(x), el polimonio que cumple toda la regla \nP(x) = Lo * Y0 + L1 * Y1 + L2 * Y2")
p = expand(2*l0+5*l1+3*l2)
p
print('remplazando x por el valor de 3, hallamos P(3)')
p.subs(x,3)