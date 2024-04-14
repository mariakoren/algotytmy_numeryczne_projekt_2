# Algorytm A3 działa dla postawionego zadania (jeśli nie działa, tzn. proces nie zawsze jest zbieżny do rozwiązania, to wskaż przykłady, gdy jest rozbieżny).
import numpy as np
import os, sys

# Sciezka do folderu rodzicac
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from podstawowa import *
from a3 import gauss_seidl

def calculate_err(result, seidl):
    errors = result - seidl
    mean_abs_error = np.mean(np.abs(errors))
    max_abs_error = np.max(np.abs(errors))

    # jesli jakis element w result = 0 - wywala go z obu zbiorow
    non_zero_res = result[result != 0]
    non_zero_errs = errors[result != 0]
    mean_percentage_abs_err = np.mean(np.abs(non_zero_errs) / np.abs(non_zero_res)) * 100

    return mean_abs_error, max_abs_error, mean_percentage_abs_err

def test_h2(matrix, vector):
    seidl_propabilities = gauss_seidl(np.array(matrix), np.array(vector))
    result = np.linalg.solve(np.array(matrix), np.array(vector))
    print("\nWyniki dla algorytmu Gaussa Seidla: \n")
    print(seidl_propabilities)
    print("\nWyniki wbudowanej funkcji: \n")
    print(result)

    mean_abs_err, max_abs_err, mean_percentage = calculate_err(result, seidl_propabilities)

    print("\n------------------------------------")
    print("\nRóżnice wartości między algorytmami:")
    print(f"Średnia różnica wyników: {mean_abs_err}")
    print(f"Średnia różnica wyników procentowo: {mean_percentage} %")
    print(f"Max różnica wyników: {max_abs_err}")

matrix, vector = main()
test_h2(matrix, vector)