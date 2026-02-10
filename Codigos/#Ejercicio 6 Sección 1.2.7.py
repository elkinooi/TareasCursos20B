#Ejercicio 6 Sección 1.2.7

import sympy as sp
from sympy import Matrix, acos, pi, N, symbols, linsolve

# -----------------------
# Bases canónicas
# -----------------------
e1 = Matrix([1,0,0])
e2 = Matrix([0,1,0])
e3 = Matrix([0,0,1])

# -----------------------
# Vectores
# -----------------------
a = Matrix([1,2,3])
b = Matrix([4,5,6])
c = Matrix([3,2,1])
d = Matrix([6,5,4])

# -----------------------
# Sumas de vectores
# -----------------------
print("----- Sumas de vectores -----")
print("a + b + c + d =", a + b + c + d)
print("a + b - c - d =", a + b - c - d)
print("a - b + c - d =", a - b + c - d)
print("-a + b - c + d =", -a + b - c + d)

# -----------------------
# Sumas de vectores
# -----------------------
print("-----\nÁngulos entre vectores y bases -----")
def angle_between(u, v):
    cos_theta = u.dot(v) / (u.norm() * v.norm())
    theta_rad = acos(cos_theta)
    theta_deg = theta_rad * 180 / pi
    return N(theta_deg)

# Ángulos para a
angulo_a_e1 = angle_between(a, e1)
angulo_a_e2 = angle_between(a, e2)
angulo_a_e3 = angle_between(a, e3)

# Ángulos para b
angulo_b_e1 = angle_between(b, e1)
angulo_b_e2 = angle_between(b, e2)
angulo_b_e3 = angle_between(b, e3)

# Ángulos para c
angulo_c_e1 = angle_between(c, e1)
angulo_c_e2 = angle_between(c, e2)
angulo_c_e3 = angle_between(c, e3)

# Ángulos para d
angulo_d_e1 = angle_between(d, e1)
angulo_d_e2 = angle_between(d, e2)
angulo_d_e3 = angle_between(d, e3)

# Mostrar resultados
print("----- Ángulos de a con e1, e2, e3 -----")
print("a · e1 =", angulo_a_e1, "°")
print("a · e2 =", angulo_a_e2, "°")
print("a · e3 =", angulo_a_e3, "°")

print("\n----- Ángulos de b con e1, e2, e3 -----")
print("b · e1 =", angulo_b_e1, "°")
print("b · e2 =", angulo_b_e2, "°")
print("b · e3 =", angulo_b_e3, "°")

print("\n----- Ángulos de c con e1, e2, e3 -----")
print("c · e1 =", angulo_c_e1, "°")
print("c · e2 =", angulo_c_e2, "°")
print("c · e3 =", angulo_c_e3, "°")

print("\n----- Ángulos de d con e1, e2, e3 -----")
print("d · e1 =", angulo_d_e1, "°")
print("d · e2 =", angulo_d_e2, "°")
print("d · e3 =", angulo_d_e3, "°")

# -----------------------
# Normas de los vectores
# -----------------------
print("\n----- Normas de vectores -----")
print("||a|| =", a.norm())
print("||b|| =", b.norm())
print("||c|| =", c.norm())
print("||d|| =", d.norm())

# -----------------------
# Ángulos entre vectores
# -----------------------
def angle_between(u, v):
    cos_theta = u.dot(v) / (u.norm() * v.norm())
    theta_rad = acos(cos_theta)
    theta_deg = theta_rad * 180 / pi
    return N(theta_deg)

print("\n----- Ángulos entre vectores -----")
print("Ángulo entre a y b =", angle_between(a, b), "°")
print("Ángulo entre c y d =", angle_between(c, d), "°")

# -----------------------
# Proyección de a sobre b
# -----------------------
proy = (a.dot(b) / b.dot(b)) * b
print("\n----- Proyección -----")
print("Proyección de a sobre b =", proy)

# -----------------------
# Verificar coplanaridad
# -----------------------
alpha, beta, gamma = symbols('alpha beta gamma')
ecuaciones = [
    alpha*a[0] + beta*b[0] + gamma*c[0] - d[0],
    alpha*a[1] + beta*b[1] + gamma*c[1] - d[1],
    alpha*a[2] + beta*b[2] + gamma*c[2] - d[2]
]
sol = linsolve(ecuaciones, (alpha, beta, gamma))
print("\n----- Coplanaridad -----")
print("Solución del sistema:", sol)
if sol != sp.EmptySet:
    print("Los vectores a, b, c y d son coplanares")

# -----------------------
# Producto punto (a + b) · (c + d)
# -----------------------
resultado = (a + b).dot(c + d)
print("\n----- Producto punto -----")
print("(a + b) · (c + d) =", resultado)

# -----------------------
# Productos cruz y ángulos con d
# -----------------------
a_cross_b = a.cross(b)
b_cross_c = b.cross(c)
c_cross_d = c.cross(d)

print("\n----- Productos cruz -----")
print("a × b =", a_cross_b)
print("b × c =", b_cross_c)
print("c × d =", c_cross_d)

print("\n----- Ángulos entre vector cruz y d -----")
print("Ángulo entre a×b y d =", angle_between(a_cross_b, d), "°")
print("Ángulo entre b×c y d =", angle_between(b_cross_c, d), "°")
print("Ángulo entre c×d y d =", angle_between(c_cross_d, d), "°")

# -----------------------
# Producto mixto c · (a × b)
# -----------------------
mixed_product = c.dot(a_cross_b)
print("\n----- Producto mixto -----")
print("c · (a × b) =", mixed_product)
if mixed_product == 0:
    print("Los vectores a, b, c son coplanarios (volumen = 0)")
