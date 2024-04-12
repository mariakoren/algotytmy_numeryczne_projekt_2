import numpy as np

# JESZCZE TROCHE TO POZMIENIAM

def gauss_elimination_with_partial_pivoting(matrix_1, matrix_2):

    if matrix_1.shape[0] != matrix_1.shape[1]:
        print("ERROR: Square matrix not given!")
        return
    if matrix_2.shape[1] > 1 or matrix_2.shape[0] != matrix_1.shape[0]:
        print("ERROR: Constant vector incorrectly sized")
        return

    n=len(matrix_2)
    m=n-1
    i=0
    j=i-1
    x=np.zeros(n)
    new_line="/n"

    augmented_matrix = np.concatenate((matrix_1, matrix_2,), axis=1, dtype=float)
    print(f"the initial augmented matrix is: {new_line}{augmented_matrix}")
    print("solving for the upper-triangular matrix:")
    
    
    #partial pivoting:
    while i<n:
        max_row_index = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_row_index]] = augmented_matrix[[max_row_index, i]]
        
        if augmented_matrix[i][i]==0.0:
            print("Divide by zero error")
            return
        for j in range(i+1,n):
            scaling_factor=augmented_matrix[j][i]/augmented_matrix[i][i]
            augmented_matrix[j]=augmented_matrix[j]-(scaling_factor * augmented_matrix[i])
            print(augmented_matrix)
            
        i=i+1
    
        x[m]=augmented_matrix[m][n]/augmented_matrix[m][m]
        for k in range(n-2,-1,-1):
            x[k]=augmented_matrix[k][n]
            for j in range(k+1,n):
                x[k]=x[k]/augmented_matrix[k][k]
    
    print("The following x vector matrix solves the above augmented matrix:")
    for answer in range(n):
        print(f"x{answer} is {x[answer]}")


# Trzeba zakomentować żeby dało się importować bez wywoływania kodu poniżej

# variable_matrix = np.array([[1, 1, 3], [0, 1, 3], [-1, 3, 0]])
# constant_matrix = np.array([[1], [3], [5]])

# gauss_elimination_with_partial_pivoting(variable_matrix, constant_matrix)