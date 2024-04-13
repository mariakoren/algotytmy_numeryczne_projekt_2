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

matrix1= copy.deepcopy(matrix)
matrix2 = copy.deepcopy(matrix)
matrix3 = copy.deepcopy(matrix)

vector1 = copy.deepcopy(vector)
vector2 = copy.deepcopy(vector)
vector3 = copy.deepcopy(vector)

res1 = gauss(matrix1, vector1)
res2 = gauss_elimination_partial_pivoting(np.array(matrix2), np.array(vector2))
res3 = gauss_seidl(np.array(matrix3), np.array(vector3))

print(res1)
print()
print(res2)
print()
print(res3)
