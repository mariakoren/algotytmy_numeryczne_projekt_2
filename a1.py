# algorytm eliminacji Gaussa bez wyboru elementu podstawowego

def alg1(macierz):
    for k in range(len(macierz)-1):
        for i in range(1, len(macierz)):
            w=macierz[i]
            if macierz[k][k] != 0:
                m =macierz[i][k]/macierz[k][k]
                for j in range(len(macierz[i])):
                    # print(macierz[i][j], end =" ")
                    macierz[i][j] = macierz[i][j] - m*w[j]
                    print_matrix(macierz)

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end =" ")
        print()
    print()




alg1([[2, 4, 6],[2, 4, 8],[1, 2, 3]])
