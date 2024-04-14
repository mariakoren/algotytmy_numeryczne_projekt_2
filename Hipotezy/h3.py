# Jeśli Algorytm A3 jest zbieżny do rozwiązania, to wyniki otrzymujemy istotnie szybciej niż dla A1 i A2.
import time
import numpy as np
import os, sys

# Sciezka do folderu rodzica
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a1 import gauss
from a2 import gauss_elimination_partial_pivoting
from a3 import gauss_seidl

from podstawowa import *

def performanceTest(function, *args):
    start = time.time()
    result = function(*args)
    stop = time.time()
    runTime = stop - start

    return (result, runTime)

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


# zrobione że można puszczać listy argumentów do przetestowania
def test(matrtix, vector):

    testResults = testRuntime([[(matrix, vector)], [(np.array(matrix), np.array(vector))], [(np.array(matrix), np.array(vector))]], [gauss, gauss_elimination_partial_pivoting, gauss_seidl])

    for key, values in testResults.items():
        results = []
        times = []

        for elem in values:
            results.append(elem[0])
            times.append(elem[1])

        avg_time = sum(times) / len(times)

        print("\n", "-----------------------------------------------------------------------")
        print(f"Algorytm {key}:")
        print("Wyniki: ")
        print(results, "\n")
        print("Czasy wykonania: ")
        print(times, "\n")
        print("Średni czas wykonania: ", avg_time)

matrix, vector = main()
test(matrix, vector)
