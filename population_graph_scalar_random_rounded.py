# Population of pademelons/thylacines is multiplied by a scalar every unit of time
# Models external events such as natural disasters
# that randomly affect the entire pademelon/thylacine population

from population_graph_functions import *

random_max = 0.1

result = framework(rand_max=random_max, rounded=True)

draw(result[0], result[1],  "Population Change Over Time (0.10 Randomness)")

# draw_relative(calc_relative(result[0], result[1]), "Relative Population Change Over Time (0.10 Randomness)")
