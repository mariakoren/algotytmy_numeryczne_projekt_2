import time
import os, sys
import numpy as np
import copy
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from podstawowa import *
from montecarlo import *
from a1 import gauss
from a2 import gauss_elimination_partial_pivoting


# matrix, vector = main()

matrix = [[random.randint(1, 1000) for _ in range(100)] for _ in range(100)]
vector = [random.randint(1, 1000) for _ in range(100)]

matrix1= copy.deepcopy(matrix)
matrix2 = copy.deepcopy(matrix)
vector1 = copy.deepcopy(vector)
vector2 = copy.deepcopy(vector)

# slownik, osk, exit, start = prepare_for_monte_carlo()

# size = len(matrix)
# results_from_montecarlo = []
# for i in range(1, size+1):
#     results_from_montecarlo.append(monte_carlo(slownik, i, exit, osk, 100)[0])

res1 = gauss(matrix1, vector1)
res2 = gauss_elimination_partial_pivoting(np.array(matrix2), np.array(list(map(lambda x: [x], vector2))))

# # pierwszy zestaw
# diff = []
# for i in range(len(results_from_montecarlo)):
#     diff.append((res1[i] - results_from_montecarlo[i])-(res2[i] - results_from_montecarlo[i]))
# srednia = sum(diff)/len(diff)
# print(diff) # [0.0, 0.0, 0.0, -2.7755575615628914e-17, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.7755575615628914e-17, 0.0, 2.7755575615628914e-17, 2.7755575615628914e-17, 0.0, -2.7755575615628914e-17, -2.7755575615628914e-17, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# print(srednia) # 0.0


# drugi zestaw
# diff = []
# for i in range(len(results_from_montecarlo)):
#     diff.append((res1[i] - results_from_montecarlo[i])-(res2[i] - results_from_montecarlo[i]))
# print(diff) # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# macierz 100 na 100, o ile ta macierz jest macierzą, monte carlo nie możemy stosować
x = np.linalg.solve(np.array(matrix), np.array(vector))
diff = []
for i in range(len(x)):
    diff.append((res2[i] - x[i])-(res1[i] - x[i]))
# print(diff) 
srednia = sum(diff)/len(diff)
print(srednia) # -0.00010820278647168613



