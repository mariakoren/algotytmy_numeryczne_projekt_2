import time
import os, sys
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from podstawowa import *
from a1 import alg1
from a2 import gauss_elimination_with_partial_pivoting
from a3 import gauss_seidl
matrix, vector = main()

res1 = alg1(matrix, vector)
res2 = gauss_elimination_with_partial_pivoting(np.array(matrix), np.array(list(map(lambda x: [x], vector))))
res3 = gauss_seidl(np.array(matrix), np.array(vector))

print(res1)
print()
print(res2)
print()
print(res3)
