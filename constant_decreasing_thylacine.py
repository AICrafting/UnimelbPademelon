import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random

alph = 0.15
bet = 0.003
lam = 0.18
omeg = 0.0016
thylacine_decrease = 0.073
thylacine_extinct = False


def check_boundaries(population):
    if population > 1000:
        return 1000
    if population < 0:
        return 0
    else:
        return population


def model(p, t):
    x,y = p
    dxdt = alph * x - bet * x * y
    if not thylacine_extinct:
        dydt = - lam * y + omeg * x * y
    else:
        dydt = 0
    return [dxdt, dydt]


x0 = 180
y0 = 30

iterations = 1100
iterations_const = iterations

pademelon_list = []
thylacine_list = []

while iterations > 0:
    t = np.linspace(iterations_const - iterations, iterations_const - iterations + 1, 11)

    population_values = odeint(model, [x0, y0], t)

    pademelon_population = population_values[:, 0]
    thylacine_population = population_values[:, 1]

    pademelon_list_temp = list(pademelon_population)
    for x in pademelon_list_temp:
        pademelon_list.append(check_boundaries(x))
    pademelon_list.pop()
    x0 = check_boundaries(pademelon_list_temp[10])

    thylacine_list_temp = list(thylacine_population)
    for y in thylacine_list_temp:
        thylacine_list.append(check_boundaries(y))
    thylacine_list.pop()
    y0 = check_boundaries(thylacine_list_temp[10] - thylacine_decrease)
    if y0 == 0:
        thylacine_extinct = True
    iterations-=1

t = np.linspace(0, iterations_const, iterations_const * 10)

plt.figure(figsize=(10,6))
plt.plot(t, pademelon_list, label="Pademelon Population")
plt.plot(t, thylacine_list, label="Thylacine Population")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Population Change Over Time (0.073 Thylacines Hunted every 1 Unit of Time)")
plt.legend()
plt.grid(True)
plt.show()