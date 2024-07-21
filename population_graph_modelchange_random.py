# Smooth curve - use rounded for lifelike results (no fractional animals)

from population_graph_functions import *

random_model_max = 0.1

result = framework(initialise_scalar=True, rand_model_scalar=random_model_max, rounded=False)

draw(result[0], result[1], "Population Change Over Time (0.10 Randomness Smooth)")

draw_relative(calc_relative(result[0], result[1]), "Relative Population Over Time (0.10 Randomness Smooth)")