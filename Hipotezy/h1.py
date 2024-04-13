import time
import os, sys
import numpy as np
import copy
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from podstawowa import *
from a1 import gauss
from a2 import gauss_elimination_partial_pivoting
from a3 import gauss_seidl
matrix, vector = main()

# matrix = [[1.2,  2.6, -0.1,  1.5],
#            [4.5,  9.8, -0.4,  5.7],
#            [0.1, -0.1, -0.3, -3.5],
#            [4.5, -5.2,  4.2, -3.4]]
# vector = [13.15, 49.84, -14.08, 46.51]



matrix1= copy.deepcopy(matrix)
matrix2 = copy.deepcopy(matrix)
matrix3 = copy.deepcopy(matrix)

vector1 = copy.deepcopy(vector)
vector2 = copy.deepcopy(vector)
vector3 = copy.deepcopy(vector)

res1 = gauss(matrix1, vector1)
res2 = gauss_elimination_partial_pivoting(np.array(matrix2), np.array(list(map(lambda x: [x], vector2))))
res3 = gauss_seidl(np.array(matrix3), np.array(vector3))

# print(res1)
print()
print(res2)
print()
# print(res3)