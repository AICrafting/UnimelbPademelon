import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random

alph = 0.15
bet = 0.003
lam = 0.18
omeg = 0.0016
random_max = 0.4
pademelon_extinct = False
thylacine_extinct = False


def model(p, t, pademelon_extinct, thylacine_extinct):
    x,y = p
    if not pademelon_extinct:
        dxdt = alph * x - bet * x * y
    else:
        dxdt = 0
    if not thylacine_extinct:
        dydt = - lam * y + omeg * x * y
    else:
        dydt = 0
    return [dxdt, dydt]

def check_boundaries(population):
    if population > 1000:
        return 1000
    if population < 0:
        return 0
    else:
        return population


def check_for_extinction(population):
    if population <= 0:
        return True
    else:
        return False

x0 = 180
y0 = 30

iterations = 100

pademelon_list = []
thylacine_list = []

while iterations > 0:
    t = np.linspace(100 - iterations, 101 - iterations, 11)

    population_values = odeint(model, [x0, y0], t, (pademelon_extinct, thylacine_extinct))

    pademelon_population = population_values[:, 0]
    thylacine_population = population_values[:, 1]

    pademelon_list_temp = list(pademelon_population)
    for x in pademelon_list_temp:
        integer = check_boundaries(x)
        integer = round(integer, 0)
        if not pademelon_extinct:
            pademelon_extinct = check_for_extinction(integer)
            pademelon_list.append(integer)
        else:
            pademelon_list.append(0)
    pademelon_list.pop()
    x0 = check_boundaries(check_boundaries(pademelon_list_temp[10]) * (1 - random_max + random.randint(0, 100) / 50 * random_max))

    thylacine_list_temp = list(thylacine_population)
    for y in thylacine_list_temp:
        integer = check_boundaries(y)
        integer = round(integer, 0)
        if not thylacine_extinct:
            thylacine_extinct = check_for_extinction(integer)
            thylacine_list.append(integer)
        else:
            thylacine_list.append(0)
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
