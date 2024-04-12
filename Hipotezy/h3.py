# Jeśli Algorytm A3 jest zbieżny do rozwiązania, to wyniki otrzymujemy istotnie szybciej niż dla A1 i A2.
import time
import os, sys

# Sciezka do folderu rodzica
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a1 import alg1   # TODO: POPRAWIC NAZWA FUNKCJI - POZNIEJ OGARNE - mati
from a2 import gauss_elimination_with_partial_pivoting
from a3 import gauss_seidl

def performanceTest(function, *args):
    start = time.time()
    result = function(*args)
    stop = time.time()
    runTime = start - stop

    return (result, runTime)

def startTests(cases, functions):
    results = {}

    for i in range(0, functions.len()):
        fun = functions[i]
        funcName = fun.__name__
        results[funcName] = []

        for case in cases[i]:
            result = performanceTest(fun, case)
            results[funcName].append(result)

    return results

# arg:1 lista z trzema listami dla argumentów dla testów dla każdej funkcji, arg:2 lista z funkcjami do testów
startTests([[], [], []], [alg1, gauss_elimination_with_partial_pivoting, gauss_seidl])