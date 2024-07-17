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

pademelon_list = list(pademelon_population)
for x in pademelon_list:
    pademelon_list[pademelon_list.index(x)] = round(x , 0)
pademelon_population_final = tuple(pademelon_list)
thylacine_list = list(thylacine_population)
for y in thylacine_list:
    thylacine_list[thylacine_list.index(y)] = round(y, 0)
thylacine_population_final = tuple(thylacine_list)

plt.figure(figsize=(10,6))
plt.plot(t, pademelon_population_final, label="Pademelon Population")
plt.plot(t, thylacine_population_final, label="Thylacine Population")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Population Change Over Time")
plt.legend()
plt.grid(True)
plt.show()
