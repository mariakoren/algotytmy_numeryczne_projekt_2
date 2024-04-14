import time
import os, sys
import numpy as np
import copy
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from podstawowa import *
from montecarlo import *
from a1 import gauss
from a2 import gauss_elimination_partial_pivoting


matrix, vector = main()
matrix1= copy.deepcopy(matrix)
matrix2 = copy.deepcopy(matrix)
vector1 = copy.deepcopy(vector)
vector2 = copy.deepcopy(vector)

slownik, osk, exit, start = prepare_for_monte_carlo()

size = len(matrix)
results_from_montecarlo = []
for i in range(1, size+1):
    results_from_montecarlo.append(monte_carlo(slownik, i, exit, osk, 1000)[0])

res1 = gauss(matrix1, vector1)
res2 = gauss_elimination_partial_pivoting(np.array(matrix2), np.array(list(map(lambda x: [x], vector2))))


print(results_from_montecarlo)
print()
print(res1)
print()
print(res2)
