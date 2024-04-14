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

# matrix = [[random.randint(1, 1000) for _ in range(100)] for _ in range(100)]
# vector = [random.randint(1, 1000) for _ in range(100)]

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

# print(res1)

# pierwszy zestaw
diff1 = []
diff2 = []
for i in range(len(results_from_montecarlo)):
    diff1.append(res1[i] - results_from_montecarlo[i])
    diff2.append(res2[i] - results_from_montecarlo[i])
srednia1 = sum(diff1)/len(diff1)
srednia2 = sum(diff2)/len(diff2)
print(srednia1) # -0.005589991928975173  0.0006004842615010156 -0.001254548059016288 -0.0007977564729658342
print(srednia2) # -0.005589991928975175  0.000600484261501013 -0.0012545480590162794 -0.0007977564729659226




# macierz 100 na 100, o ile ta macierz jest macierzą zwykłą, monte carlo nie możemy stosować
# diff1 = []
# diff2 = []
# x = np.linalg.solve(np.array(matrix), np.array(vector))
# for i in range(len(x)):
#     diff1.append(res1[i] - x[i])
#     diff2.append(res2[i] - x[i])

# srednia1 = sum(diff1)/len(diff1)
# print(srednia1) 

# srednia2 = sum(diff2)/len(diff2)
# print(srednia2) 





