# Implements all 3 types of randomness i.e.
# 1 - External randomness - Natural disasters
# 2 - Internal randomness - Diseases/Fertility
# 3 - Internal randomness - Migration

from population_graph_functions import *

random_max = 0.1
random_model_max = 0.1
rand_constant = 5

result = framework(initialise_scalar=True, rand_model_scalar=random_model_max, rand_const_max=rand_constant, rand_max=random_max, rounded=False)

draw(result[0], result[1], "Population Change Over Time (3 Types Of Randomness)")

draw_relative(calc_relative(result[0], result[1]), "Relative Population Over Time (3 Types Of Randomness)")
