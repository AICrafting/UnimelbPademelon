# Model is redefined every unit of time - smoother transition
# Parameters are multiplied by random scalars - symbolises internal randomness
# such as from diseases or larger fertility in the populations that would impact their
# intrinsic growth rate and natural death rate

from population_graph_functions import *

random_model_max = 0.1

result = framework(initialise_scalar=True, rand_model_scalar=random_model_max, rounded=True)

draw(result[0], result[1], "Population Change Over Time (0.10 Randomness Smooth)")

# draw_relative(calc_relative(result[0], result[1]), "Relative Population Over Time (0.10 Randomness Smooth)")
