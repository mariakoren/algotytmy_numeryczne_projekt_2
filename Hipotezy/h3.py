# Jeśli Algorytm A3 jest zbieżny do rozwiązania, to wyniki otrzymujemy istotnie szybciej niż dla A1 i A2.
import time
import numpy as np
import os, sys

# Sciezka do folderu rodzica
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a1 import gauss
from a2 import gauss_elimination_partial_pivoting
from a3 import gauss_seidl

def performanceTest(function, *args):
    start = time.time()
    result = function(*args)
    stop = time.time()
    runTime = stop - start

    ## DO WYBORU CZY MA ZWRACAC TYLKO CZASY CZY TEZ WYNIKI
    return (result, runTime)
    # return runTime

def testRuntime(cases, functions):
    results = {}

    for i in range(0, len(functions)):
        fun = functions[i]
        funcName = fun.__name__
        results[funcName] = []

        for case in cases[i]:
            result = performanceTest(fun, *case)
            results[funcName].append(result)

    return results

def test():
    M1 = [
        [12.0,  1.2,  0.5,  0.3,  0.4,  0.1,  0.6,  0.7,  0.4,  0.3],
        [ 0.8, 15.0,  0.6,  1.1,  0.3,  0.8,  0.2,  0.1,  0.5,  0.4], 
        [ 1.1,  0.5,  9.0,  0.8,  0.5,  0.1,  0.8,  0.2,  1.2,  0.9],
        [ 0.3,  0.9,  0.7, 13.0,  0.2,  1.1,  0.3,  0.6,  0.1,  0.4],
        [ 0.6,  0.2,  1.4,  0.7, 16.0,  0.9,  0.4,  0.1,  0.2,  0.5],
        [ 0.5,  0.3,  0.6,  0.3,  0.5, 10.0,  0.6,  1.3,  0.2,  1.1],
        [ 0.9,  0.4,  0.7,  1.1,  0.3,  0.8, 14.0,  0.1,  0.9,  0.2],
        [ 0.2,  0.8,  0.5,  0.9,  0.7,  0.4,  0.5, 11.0,  0.7,  0.3],
        [ 1.3,  0.3,  0.4,  0.8,  0.1,  1.2,  0.4,  0.6, 12.0,  0.1],
        [ 0.2,  0.5,  0.3,  0.4,  1.2,  0.3,  0.8,  0.7,  0.6, 15.0]
    ]
    V1 = [15.7, 18.3, 15.4, 17.3, 20.5, 14.7, 16.1, 13.9, 17.7, 18.9]

    M2 = [
        [ 8.0,  0.5,  1.2,  0.3,  1.0,  0.6,  2.1,  1.2,  0.7,  0.2],
        [ 0.5,  9.0,  0.2,  1.8,  0.1,  0.9,  0.3,  0.4,  1.7,  2.1],
        [ 1.2,  0.2,  6.0,  0.8,  2.3,  0.5,  0.9,  0.6,  0.3,  1.1],
        [ 0.3,  1.8,  0.8, 10.0,  0.6,  0.2,  1.6,  0.8,  2.1,  0.4],
        [ 1.0,  0.1,  2.3,  0.6,  7.0,  1.2,  0.1,  1.6,  0.6,  0.3],
        [ 0.6,  0.9,  0.5,  0.2,  1.2,  9.0,  0.4,  0.2,  0.9,  1.6],
        [ 2.1,  0.3,  0.9,  1.6,  0.1,  0.4,  7.0,  0.4,  1.6,  2.2], 
        [ 1.2,  0.4,  0.6,  0.8,  1.6,  0.2,  0.4,  6.0,  0.1,  0.7],
        [ 0.7,  1.7,  0.3,  2.1,  0.6,  0.9,  1.6,  0.1,  8.0,  0.8],
        [ 0.2,  2.1,  1.1,  0.4,  0.3,  1.6,  2.2,  0.7,  0.8, 10.0] 
    ]
    V2 = [24.5, 30.4, 25.5, 35.1, 29.2, 28.3, 28.4, 21.7, 29.9, 35.4]

    M3 = [
        [ 8.0,  2.1,  0.5,  0.3,  0.4,  0.1,  0.6,  0.7,  0.9,  0.5],
        [ 1.2,  6.0,  0.6,  1.1,  0.8,  0.8,  0.2,  0.1,  0.5,  1.3], 
        [ 1.1,  0.5,  7.0,  0.5,  0.9,  0.1,  0.8,  0.2,  1.2,  0.3],
        [ 0.3,  0.9,  0.7,  9.0,  1.2,  1.1,  0.3,  0.6,  0.1,  0.2],
        [ 0.6,  2.2,  0.4,  0.7, 10.0,  0.9,  0.4,  0.1,  0.2,  0.6],
        [ 0.5,  0.3,  0.8,  0.8,  0.9,  8.0,  0.8,  1.3,  0.2,  1.1],
        [ 0.9,  0.9,  0.7,  0.1,  0.8,  0.8, 12.0,  0.8,  0.5,  0.8],
        [ 0.6,  0.5,  0.2,  0.4,  0.7,  0.4,  0.3,  5.0,  0.7,  0.2],
        [ 0.1,  0.3,  0.6,  0.8,  0.1,  0.6,  0.9,  0.6,  7.0,  0.9],
        [ 0.3,  0.2,  0.8,  0.4,  1.2,  0.3,  0.4,  0.3,  0.4,  6.0] 
    ]
    V3 =[28.2, 20.1, 21.7, 27.6, 34.6, 27.7, 38.1, 19.7, 22.2, 20.8]

    testResults = testRuntime([[(M1, V1), (M2, V2), (M3, V3)], [], [(np.array(M1), np.array(V1)), (np.array(M2), np.array(V2)), (np.array(M3), np.array(V3))]], [gauss, gauss_elimination_partial_pivoting, gauss_seidl])

    print(testResults)

test()
