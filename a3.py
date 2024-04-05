import numpy as np


def gauss_seidl(matrix, vector, max_iter=1000, tol=1e-6):
    n = len(matrix)
    x = np.zeros(n)
    for _ in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s1 = np.dot(matrix[i, :i], x_new[:i])
            s2 = np.dot(matrix[i, i + 1:], x[i + 1:])
            x_new[i] = (vector[i] - s1 - s2) / matrix[i, i]
        if np.allclose(x, x_new, atol=tol):
            return x_new
        x = x_new
    return x


test_matrix = np.array([[10, -1, 2, 0],
                        [-1, 11, -1, 3],
                        [2, -1, 10, -1],
                        [0.0, 3, -1, 8]])

test_vector = np.array([6, 25, -11, 15])
test_result = gauss_seidl(test_matrix, test_vector)

print(test_result)
