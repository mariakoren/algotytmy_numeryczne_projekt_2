import numpy as np


def gauss_elimination_partial_pivoting(matrix, vector):
    m_set = np.concatenate((matrix, vector.reshape(-1, 1)), axis=1)
    vector_len = len(vector)

    for i in range(vector_len - 1):
        pivot = np.argmax(abs(m_set[i:, i])) + i
        if pivot != i:
            m_set[[i, pivot]] = m_set[[pivot, i]]

        for y in range(i + 1, vector_len):
            line = m_set[y, i] / m_set[i, i]
            m_set[y] = m_set[y].astype(np.float64) - line * m_set[i].astype(np.float64)

    solution = [0] * vector_len
    for i in range(vector_len - 1, -1, -1):
        solution[i] = (m_set[i][vector_len] - np.dot(m_set[i, :vector_len], solution)) / m_set[i][i]

    return solution

# # DO TESTU
# A = np.array([[1, 2, 1],
#             [3, 1, -2],
#             [2, -3, 4]])
# B = np.array([6, 5, 1])

# M3 = np.array([
#         [ 8.0,  2.1,  0.5,  0.3,  0.4,  0.1,  0.6,  0.7,  0.9,  0.5],
#         [ 1.2,  6.0,  0.6,  1.1,  0.8,  0.8,  0.2,  0.1,  0.5,  1.3], 
#         [ 1.1,  0.5,  7.0,  0.5,  0.9,  0.1,  0.8,  0.2,  1.2,  0.3],
#         [ 0.3,  0.9,  0.7,  9.0,  1.2,  1.1,  0.3,  0.6,  0.1,  0.2],
#         [ 0.6,  2.2,  0.4,  0.7, 10.0,  0.9,  0.4,  0.1,  0.2,  0.6],
#         [ 0.5,  0.3,  0.8,  0.8,  0.9,  8.0,  0.8,  1.3,  0.2,  1.1],
#         [ 0.9,  0.9,  0.7,  0.1,  0.8,  0.8, 12.0,  0.8,  0.5,  0.8],
#         [ 0.6,  0.5,  0.2,  0.4,  0.7,  0.4,  0.3,  5.0,  0.7,  0.2],
#         [ 0.1,  0.3,  0.6,  0.8,  0.1,  0.6,  0.9,  0.6,  7.0,  0.9],
#         [ 0.3,  0.2,  0.8,  0.4,  1.2,  0.3,  0.4,  0.3,  0.4,  6.0] 
#     ])
# V3 = np.array([28.2, 20.1, 21.7, 27.6, 34.6, 27.7, 38.1, 19.7, 22.2, 20.8])

# test = gauss_elimination_partial_pivoting(M3, V3)

# print(test)