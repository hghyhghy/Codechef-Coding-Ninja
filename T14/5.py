# trnaspose a given matrix

def transpose(matrix):
    
    row=len(matrix)
    column=len(matrix[0])

    transposed =[[0]* row for _ in range(column)]

    for i in range(row):
        
        for j in range(column):
            
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = transpose(matrix)
print("Transposed Matrix:")
for row in transposed:
    print(row)