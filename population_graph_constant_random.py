# Smooth curve - use rounded for lifelike results (no fractional animals)

import numpy as np
from scipy.integrate import odeint
from population_graph_functions import *

random_dict["constant"] = True


def model(p, t, pademelon_extinct, thylacine_extinct):
    x, y = p
    if not pademelon_extinct:
        dxdt = alph * x - bet * x * y
    else:
        #Ensure that pademelon population remains 0 after species is driven to extinction
        dxdt = 0
    if not thylacine_extinct:
        dydt = - lam * y + omeg * x * y
    else:
        # Ensure that thylacine population remains 0 after species is driven to extinction
        dydt = 0
    return [dxdt, dydt]


iterations = 100

pademelon_list = []
thylacine_list = []

while iterations > 0:
    t = np.linspace(100 - iterations, 101 - iterations, 11)

    population_values = odeint(model, [x0, y0], t, (pademelon_extinct, thylacine_extinct))

    pademelon_population = population_values[:, 0]
    thylacine_population = population_values[:, 1]

    x0 = format_list(pademelon_population, pademelon_list, 0, "pademelon")
    y0 = format_list(thylacine_population, thylacine_list, 0, "thylacine")

    iterations -= 1

t = np.linspace(0, 100, 1000)

draw(pademelon_list, thylacine_list, t, "Population Change Over Time (Random Constant)")