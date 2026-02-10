import sympy as sp

# variable de parametrización
t = sp.symbols('t', real=True)

# parametrización del círculo de radio 1
x = sp.cos(t)
y = sp.sin(t)

# campo de fuerza F = (-y/(x^2+y^2), x/(x^2+y^2))
Fx = -y/(x**2 + y**2)
Fy =  x/(x**2 + y**2)

# diferenciales
dx = sp.diff(x, t)
dy = sp.diff(y, t)

# producto punto F·dr
integrando = sp.simplify(Fx*dx + Fy*dy)

print("F·dr =", integrando)

# (a) desde 0 a π (antihorario)
Ia = sp.integrate(integrando, (t, 0, sp.pi))
trabajo_contra_a = -Ia

# (b) desde 0 a -π (horario)
Ib = sp.integrate(integrando, (t, 0, -sp.pi))
trabajo_contra_b = -Ib

print("Trabajo contra el campo (0 → π):", sp.simplify(trabajo_contra_a))
print("Trabajo contra el campo (0 → -π):", sp.simplify(trabajo_contra_b))
