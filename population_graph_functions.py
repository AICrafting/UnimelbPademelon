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

species_dict = {"pademelon": pademelon_extinct,
                "thylacine": thylacine_extinct}

random_dict = {"constant": False,
               "scalar": False}


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


def rand_const():
    return random.randint(0, 10) - 5


def format_list(population, real_list, random_max, species):
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
    if random_dict.get("scalar") & random_dict.get("constant"):
        return check_boundaries(check_boundaries(population_list_temp[10] + rand_const()) * rand_scalar(random_max))
    elif random_dict.get("scalar"):
        return check_boundaries(check_boundaries(population_list_temp[10]) * rand_scalar(random_max))
    elif random_dict.get("constant"):
        return check_boundaries(population_list_temp[10] + rand_const())
    else:
        return check_boundaries(population_list_temp[10])


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


def calc_relative(pademelon_population, thylacine_population):
    result = []
    pademelon_list = list(pademelon_population)
    thylacine_list = list(thylacine_population)
    for x in pademelon_list:
        result.append((x/thylacine_list[pademelon_list.index(x)]))
    return result

def draw_relative(relative_list, t, title="Relative Population Over Time"):
    plt.figure(figsize=(10, 6))
    plt.plot(t, relative_list, label="Pademelon to Thylacine Ratio")
    plt.xlabel("Time")
    plt.ylabel("Relative Population")
    plt.title(title)
    plt.legend()
    plt.grid("True")
    plt.show()