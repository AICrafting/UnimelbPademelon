# Smooth curve - use rounded for lifelike results (no fractional animals)

from population_graph_functions import *

result = framework(rounded=False)

draw(result[0], result[1])

# draw_relative(calc_relative(result[0], result[1]))
