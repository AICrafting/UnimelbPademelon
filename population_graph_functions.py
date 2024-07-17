import matplotlib.pyplot as plt
import random

alph = 0.15
bet = 0.003
lam = 0.18
omeg = 0.0016

x0 = 180
y0 = 30

pademelon_extinct = False
thylacine_extinct = False


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

# TODO improve format list function
def format_list(population, real_list, random_max, species):
    global pademelon_extinct, thylacine_extinct
    population_list_temp = list(population)
    for x in population_list_temp:
        integer = check_boundaries(x)
        if species == "pademelon":
            if not pademelon_extinct:
                pademelon_extinct = check_for_extinction(integer)
                real_list.append(integer)
            else:
                real_list.append(0)
        elif species == "thylacine":
            if not thylacine_extinct:
                thylacine_extinct = check_for_extinction(integer)
                real_list.append(integer)
            else:
                real_list.append(0)
    real_list.pop()
    return check_boundaries(check_boundaries(population_list_temp[10]) * rand_scalar(random_max))


def draw(pademelon_population, thylacine_population, t, title="Population Change Over Time"):
    plt.figure(figsize=(10, 6))
    plt.plot(t, pademelon_population, label="Pademelon Population")
    plt.plot(t, thylacine_population, label="Thylacine Population")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title(title)
    plt.legend()
    plt.grid("True")
    plt.show()
