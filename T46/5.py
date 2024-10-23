# Problem statement
# Bob always bragged about his smartness. To test this, Alice gave him an

# array ‘A’ of size ‘N’ and asked him to find the number of twin pairs in that array.

# A twin pair can be defined as a pair of indexes ‘x’, ‘y’ such that ‘x’ is less than ‘y’ and ‘A[y]’ - ‘A[x]’ = ‘y’ - ‘x’.

# Bob was having a hard time doing so, so he asked you to help him find the total number of twin pairs.

def count_twin_pairs(array):
    
    count = 0
    n=len(array)

    for i in range(n):
        for j in range(i+1,n):
            
            if (array[j]-array[i]) == (j-i):
                
                count += 1
                
    return count

A = [3, 4, 2, 5, 1]
print(count_twin_pairs(A))