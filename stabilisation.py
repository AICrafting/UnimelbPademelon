from scipy.optimize import fsolve

alph = 0.15
bet = 0.003
lam = 0.18
omeg = 0.0016

def equilibrium_equations(p):
    x,y = p
    eq1 = alph * x - bet * x * y
    eq2 = - lam * y + omeg * x * y
    return [eq1, eq2]

equiilibrium_points = fsolve(equilibrium_equations, [180,30])

print("Stable Population Values")
print(f"Pademelon Population (x): {equiilibrium_points[0]:.2f}")
print(f"Thylacine Population (y): {equiilibrium_points[1]:.2f}")