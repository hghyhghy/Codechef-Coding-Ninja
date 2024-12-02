# Given an ‘N’ x ‘M’ integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix. In particular, your task is to modify it in such a way that if a cell has a value 0 (matrix[i][j] == 0), then all the cells of the ith row and jth column should be changed to 0.

# You must do it in place.

def set_matrix_zeroes(matrix):
    
    column=len(matrix[0])
    row=len(matrix)

    zeroes=[]

    for i in range(row):
        
        for  j in range(column):
            
            if matrix[i][j] == 0:
                
                zeroes.append((i,j))

    for i,j in zeroes:
        
        for k in range(column):
            
            matrix[i][k] = 0
            
        for k in range(row):
            
            matrix[k][j] = 0
            
    return matrix
matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12]
]

print(set_matrix_zeroes(matrix))
