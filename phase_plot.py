import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


alph = 0.15
bet = 0.003
lam = 0.18
omeg = 0.0016

x0 = 180
y0 = 30

iterations = 100
iterations_const = iterations

pademelon_extinct = False
thylacine_extinct = False

species_dict = {"pademelon": pademelon_extinct,
                "thylacine": thylacine_extinct}

survival_dict = {"survive": 0,
                 "p_extinct": 0,
                 "t_extinct": 0,
                 "all_extinct": 0}


def model(p, t, pademelon_extinct, thylacine_extinct, scalarx1, scalarx2, scalary1, scalary2):
    x,y = p
    if not pademelon_extinct:
        dxdt = (alph * scalarx1) * x - (bet * scalarx2) * x * y
    else:
        dxdt = 0
    if not thylacine_extinct:
        dydt = - (lam * scalary1) * y + (omeg * scalary2) * x * y
    else:
        dydt = 0
    return [dxdt, dydt]

t = np.linspace(0, 100, 1000)

population_values = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 1))

population_values2 = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 0.8))

population_values3 = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 1.2))

population_values4 = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 0.6))

population_values5 = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 1.4))

population_values6 = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 0.7))

population_values7 = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 0.9))

population_values8 = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 1.1))

population_values9 = odeint(model,[x0, y0], t, (False, False, 1, 1, 1, 1.3))

f,(ax1) = plt.subplots(1)

line1, = ax1.plot(population_values[:,0], population_values[:,1], color="b", label="scalar2 = 1")
line2, = ax1.plot(population_values2[:,0], population_values2[:,1], color="r", label="scalar2 = 0.8")
line3, = ax1.plot(population_values3[:,0], population_values3[:,1], color="g", label="scalar2 = 1.2")
line4, = ax1.plot(population_values4[:,0], population_values4[:,1], color="g", label="scalar2 = 0.6")
line5, = ax1.plot(population_values5[:,0], population_values5[:,1], color="r", label="scalar2 = 1.4")
line6, = ax1.plot(population_values6[:,0], population_values6[:,1], color="b", label="scalar2 = 0.7")
line7, = ax1.plot(population_values7[:,0], population_values7[:,1], color="g", label="scalar2 = 0.9")
line8, = ax1.plot(population_values8[:,0], population_values8[:,1], color="r", label="scalar2 = 1.1")
line9, = ax1.plot(population_values9[:,0], population_values9[:,1], color="b", label="scalar2 = 1.3")

ax1.set_xlabel("Pademelon Population")
ax1.set_ylabel("Thylacine Population")

plt.title("Pademelon to Thylacine Phase Plot (Changing Omega)")

plt.show()