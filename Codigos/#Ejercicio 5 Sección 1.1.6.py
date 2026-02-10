#Ejercicio 5 Sección 1.1.6

import sympy as sp

'''ya sea para hallar el centro de masa de un cuadrado o bien de un cubo, el siguiente código 
permite calcularlo de forma sencilla siempre que se asocien bien los vertices con las masas
correspondientes a cada uno de ellos y a su vez, considerar para el caso de un cuadrado 
4 masas igual a cero analogamente con los otros 4 vertices'''

# masas
m1, m2, m3, m4, m5, m6, m7, m8 = 1, 2, 3, 4, 0, 0, 0, 0

# posiciones
r1 = sp.Matrix([0,0,0])
r2 = sp.Matrix([2,0,0])
r3 = sp.Matrix([2,2,0])
r4 = sp.Matrix([0,2,0])
r5 = sp.Matrix([0,0,0])
r6 = sp.Matrix([0,0,0])
r7 = sp.Matrix([0,0,0])
r8 = sp.Matrix([0,0,0])

# masa total
M = m1+m2+m3+m4+m5+m6+m7+m8

# centro de masa
R = (m1*r1 + m2*r2 + m3*r3 + m4*r4 + m5*r5 + m6*r6 + m7*r7 + m8*r8)/M

print("Centro de masa:")
print(sp.simplify(R))
