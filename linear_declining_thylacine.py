import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random

alph = 0.15
bet = 0.003
lam = 0.18
omeg = 0.0016
pop_decrease = 0.9

def model(p, t):
    x,y = p
    dxdt = alph * x - bet * x * y
    dydt = - lam * y + omeg * x * y
    return [dxdt, dydt]

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
        pademelon_list.append(x)
    pademelon_list.pop()
    x0 = pademelon_list_temp[10]

    thylacine_list_temp = list(thylacine_population)
    for y in thylacine_list_temp:
        thylacine_list.append(y)
    thylacine_list.pop()
    y0 = thylacine_list_temp[10] * pop_decrease
    iterations-=1

t = np.linspace(0, 100, 1000)

plt.figure(figsize=(10,6))
plt.plot(t, pademelon_list, label="Pademelon Population")
plt.plot(t, thylacine_list, label="Thylacine Population")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Population Change Over Time (10% of Thylacines Hunted every 1 Unit of Time)")
plt.legend()
plt.grid(True)
plt.show()

# As unit of time decreases sine waves merge closer together - period decreases