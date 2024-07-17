import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

alph = 0.15
bet = 0.003
lam = 0.18
omeg = 0.0016

def model(p, t):
    x,y = p
    dxdt = alph * x - bet * x * y
    dydt = - lam * y + omeg * x * y
    return [dxdt, dydt]

x0 = 180
y0 = 30

t = np.linspace(0, 100, 1000)

population_values = odeint(model, [x0, y0], t)

pademelon_population = population_values[:, 0]
thylacine_population = population_values[:, 1]

plt.figure(figsize=(10,6))
plt.plot(t, pademelon_population, label="Pademelon Population")
plt.plot(t, thylacine_population, label="Thylacine Population")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Population Change Over Time")
plt.legend()
plt.grid("True")
plt.show()