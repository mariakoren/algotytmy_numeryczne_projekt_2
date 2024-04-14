# Algorytm A3 działa dla postawionego zadania (jeśli nie działa, tzn. proces nie zawsze jest zbieżny do rozwiązania, to wskaż przykłady, gdy jest rozbieżny).
import numpy as np
import os, sys

# Sciezka do folderu rodzica
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from podstawowa import *
from a3 import gauss_seidl

def calculate_err(result, seidl):
    errors = result - seidl
    mean_abs_error = np.mean(np.abs(errors))
    max_abs_error = np.max(np.abs(errors))

    return mean_abs_error, max_abs_error

def test_h3(matrix, vector):
    seidl_propabilities = gauss_seidl(np.array(matrix), np.array(vector))
    result = np.linalg.solve(np.array(matrix), np.array(vector))
    print("\nWyniki dla algorytmu Gaussa Seidla: \n")
    print(seidl_propabilities)
    print("\nWyniki wbudowanej funkcji: \n")
    print(result)

    mean_abs_err, max_abs_err = calculate_err(result, seidl_propabilities)

    print("\n------------------------------------")
    print("\nRóżnice wartości między algorytmami:")
    print(f"Średnia różnica wyników: {mean_abs_err}")
    print(f"Max różnica wyników: {max_abs_err}")

matrix, vector = main()
test_h3(matrix, vector)