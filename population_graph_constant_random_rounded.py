# Population of pademelons/thylacines is increased/decreased
# by a constant every unit of time
# Models random migration of species from this forest to neighbouring ones

from population_graph_functions import *

rand_constant = 5

result = framework(rand_const_max=rand_constant, rounded=True)

draw(result[0], result[1], "Population Change Over Time (Random Constant)")
