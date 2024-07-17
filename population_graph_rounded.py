import numpy as np
from scipy.integrate import odeint
from population_graph_functions import *


def model(p, t):
    x,y = p
    dxdt = alph * x - bet * x * y
    dydt = - lam * y + omeg * x * y
    return [dxdt, dydt]


t = np.linspace(0, 100, 1000)

population_values = odeint(model, [x0, y0], t)

pademelon_population = population_values[:, 0]
thylacine_population = population_values[:, 1]

draw(round_element(pademelon_population), round_element(thylacine_population), t)
