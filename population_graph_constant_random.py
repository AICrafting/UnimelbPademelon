# Smooth curve - use rounded for lifelike results (no fractional animals)

from population_graph_functions import *

rand_constant = 5

result = framework(rand_const_max=rand_constant, rounded=False)

draw(result[0], result[1], "Population Change Over Time (Random Constant)")
