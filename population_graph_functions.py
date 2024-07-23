import matplotlib.pyplot as plt
import random
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

# random_dict = {"constant": False,
#                "scalar": False}


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


def round_element(population):
    population_list = list(population)
    for x in population_list:
        population_list[population_list.index(x)] = round(x, 0)
    population_final = tuple(population_list)
    return population_final


def rand_scalar(random_max):
    return 1 - random_max + random.randint(0, 100) / 50 * random_max


def rand_const(rand_constant):
    return random.randint(0, 2 * rand_constant) - rand_constant


def format_list(population, real_list, random_max, rand_constant, species):
    extinct = species_dict[species]
    population_list_temp = list(population)
    for x in population_list_temp:
        integer = check_boundaries(x)
        if not extinct:
            extinct = check_for_extinction(integer)
            species_dict[species] = extinct
            real_list.append(integer)
        else:
            real_list.append(0)
    real_list.pop()
    if extinct:
        return 0
    return check_boundaries(check_boundaries(population_list_temp[10] + rand_const(rand_constant)) * rand_scalar(random_max))


def framework(initialise_scalar=False, rand_model_scalar=0, rand_max=0, rand_const_max=0, rounded=False, x0_local=x0, y0_local=y0,
              iterations_local=iterations, pademelon_extinct_local=pademelon_extinct, thylacine_extinct_local=thylacine_extinct):

    pademelon_list = []
    thylacine_list = []

    while iterations_local > 0:
        t = np.linspace(iterations_const - iterations_local, iterations_const + 1 - iterations_local, 11)
        if initialise_scalar:
            scalarx1, scalarx2, scalary1, scalary2 = rand_scalar(rand_model_scalar), rand_scalar(rand_model_scalar), rand_scalar(rand_model_scalar), rand_scalar(rand_model_scalar)
        else:
            scalarx1, scalarx2, scalary1, scalary2 = 1, 1, 1, 1

        population_values = odeint(model, [x0_local, y0_local], t, (pademelon_extinct_local, thylacine_extinct_local,
                                                                    scalarx1, scalarx2, scalary1, scalary2))

        pademelon_population = population_values[:, 0]
        thylacine_population = population_values[:, 1]

        if rounded:
            x0_local = format_list(round_element(pademelon_population), pademelon_list, rand_max, rand_const_max, "pademelon")
            y0_local = format_list(round_element(thylacine_population), thylacine_list, rand_max, rand_const_max, "thylacine")
        else:
            x0_local = format_list(pademelon_population, pademelon_list, rand_max, rand_const_max, "pademelon")
            y0_local = format_list(thylacine_population, thylacine_list, rand_max, rand_const_max, "thylacine")

        iterations_local -= 1

    return [pademelon_list, thylacine_list]


def draw(pademelon_population, thylacine_population, title="Population Change Over Time"):
    t = np.linspace(0, iterations_const, 10 * iterations_const)
    plt.figure(figsize=(10, 6))
    plt.plot(t, pademelon_population, label="Pademelon Population")
    plt.plot(t, thylacine_population, label="Thylacine Population")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title(title)
    plt.legend()
    plt.grid("True")
    plt.show()


def calc_relative(pademelon_population, thylacine_population):
    result = []
    pademelon_list = list(pademelon_population)
    thylacine_list = list(thylacine_population)
    for x in pademelon_list:
        if thylacine_list[pademelon_list.index(x)] != 0:
            result.append((x/thylacine_list[pademelon_list.index(x)]))
        else:
            result.append(0)
    return result

def draw_relative(relative_list, title="Relative Population Over Time"):
    t = np.linspace(0, iterations_const, 10 * iterations_const)
    plt.figure(figsize=(10, 6))
    plt.plot(t, relative_list, label="Pademelon to Thylacine Ratio")
    plt.xlabel("Time")
    plt.ylabel("Relative Population")
    plt.title(title)
    plt.legend()
    plt.grid("True")
    plt.show()


def draw_slope_field():
    fig = plt.figure(1, figsize=(10, 6))
    ax = fig.add_subplot(111)

    X, Y = np.meshgrid(np.linspace(20, 980, 20), np.linspace(20, 980, 20))

    U = alph * X - bet * X * Y
    V = - lam * Y + omeg * X * Y

    N = np.sqrt(U ** 2 + V ** 2)
    U2, V2 = U / N * 50, V / N * 50
    ax.quiver(X, Y, U2, V2)

    plt.xlim([0, 1000])
    plt.ylim([0, 1000])
    plt.hlines(0, 0, 1000)
    plt.vlines(0, 0, 1000)
    plt.xlabel("Pademelon Population")
    plt.ylabel("Thylacine Population")
    plt.grid()
    plt.title("Pademelon to Thylacine Slope Field")
    plt.show()

