# Smooth curve - use rounded for lifelike results (no fractional animals)

from population_graph_functions import *

random_max = 0.1

result = framework(rand_max=random_max, rounded=False)

draw(result[0], result[1],  "Population Change Over Time (0.10 Randomness)")

# draw_relative(calc_relative(result[0], result[1]), "Relative Population Change Over Time (0.10 Randomness)")