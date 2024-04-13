# algorytm eliminacji Gaussa bez wyboru elementu podstawowego

def gauss(matrix, vector):
    for i in range(len(matrix)):
        matrix[i].append(vector[i])

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(min(rows, cols)):
        max_row = i
        for j in range(i + 1, rows):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        for j in range(i + 1, rows):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, cols):
                matrix[j][k] -= factor * matrix[i][k]

    solution = [0] * rows
    for i in range(rows - 1, -1, -1):
        solution[i] = matrix[i][cols - 1] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][cols - 1] -= matrix[j][i] * solution[i]

    return solution
    
    
# def print_matrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end =" ")
#         print()
#     print()


# Trzeba zakomentować żeby dało się importować bez wywoływania kodu poniżej
# macierz = [[1.2, 2.6, -0.1, 1.5, 13.15],
#            [4.5, 9.8, -0.4, 5.7, 49.84],
#            [0.1, -0.1, -0.3, -3.5, -14.08],
#            [4.5, -5.2, 4.2, -3.4, -46.51]]
    
# macierz = [[1, 0, 0, 0, 0, 0, 1],
#            [-0.5, 1, -0.5, 0, 0, 0, 0],
#            [0, -0.5, 1, -0.5, 0, 0, 0],
#            [0, 0, -0.5, 1, -0.5, 0, 0],
#            [0, 0, 0, -0.5, 1, -0.5, 0],
#            [0, 0, 0, 0, 0, 1, 0]]

# res = alg1(macierz)
# print(res)


