# Implements all 3 types of randomness i.e.
# 1 - External randomness - Natural disasters
# 2 - Internal randomness - Diseases/Fertility
# 3 - Internal randomness - Migration

from population_graph_functions import *

random_max = 0.2
random_model_max = 0.2
rand_constant = 2


# for i in range(0,10000):
result = framework(initialise_scalar=True, rand_model_scalar=random_model_max, rand_const_max=rand_constant, rand_max=random_max, rounded=True)
    # print(f"{i+1}/100000")

# print_surv_dict()


draw(result[0], result[1], "Population Change Over Time (3 Types Of Randomness - 2,0.2,0.2)")

# draw_relative(calc_relative(result[0], result[1]), "Relative Population Over Time (3 Types Of Randomness)")