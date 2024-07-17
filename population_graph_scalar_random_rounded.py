import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random

alph = 0.15
bet = 0.003
lam = 0.18
omeg = 0.0016
random_max = 0.5

def model(p, t):
    x,y = p
    dxdt = alph * x - bet * x * y
    dydt = - lam * y + omeg * x * y
    return [dxdt, dydt]


def check_boundaries(population):
    if population > 1000:
        return 1000
    if population < 0:
        return 0
    else:
        return population


x0 = 180
y0 = 30

iterations = 100

pademelon_list = []
thylacine_list = []

while iterations > 0:
    t = np.linspace(100 - iterations, 101 - iterations, 11)

    population_values = odeint(model, [x0, y0], t)

    pademelon_population = population_values[:, 0]
    thylacine_population = population_values[:, 1]

    pademelon_list_temp = list(pademelon_population)
    for x in pademelon_list_temp:
        integer = check_boundaries(x)
        pademelon_list.append(integer)
        pademelon_list[pademelon_list.index(integer)] = round(integer, 0)
    pademelon_list.pop()
    x0 = check_boundaries(check_boundaries(pademelon_list_temp[10]) * (1 - random_max + random.randint(0, 100) / 50 * random_max))

    thylacine_list_temp = list(thylacine_population)
    for y in thylacine_list_temp:
        integer = check_boundaries(y)
        thylacine_list.append(integer)
        thylacine_list[thylacine_list.index(integer)] = round(integer, 0)
    thylacine_list.pop()
    y0 = check_boundaries(check_boundaries(thylacine_list_temp[10]) * (1 - random_max + random.randint(0, 100) / 50 * random_max))

    iterations-=1

t = np.linspace(0, 100, 1000)

plt.figure(figsize=(10,6))
plt.plot(t, pademelon_list, label="Pademelon Population")
plt.plot(t, thylacine_list, label="Thylacine Population")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Population Change Over Time (0.10 Randomness)")
plt.legend()
plt.grid(True)
plt.show()