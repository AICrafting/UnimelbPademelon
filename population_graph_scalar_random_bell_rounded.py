import math

import numpy as np

from population_graph_functions import *

random_max = 0.2

result = framework(rand_max=random_max, rounded=True, rand_max_bell=True)

draw(result[0], result[1],  "Population Change Over Time (0.20 Randomness)")
