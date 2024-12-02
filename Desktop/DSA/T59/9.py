# Bob always bragged about his smartness. To test this, Alice gave him an

# array ‘A’ of size ‘N’ and asked him to find the number of twin pairs in that array.

# A twin pair can be defined as a pair of indexes ‘x’, ‘y’ such that ‘x’ is less than ‘y’ and ‘A[y]’ - ‘A[x]’ = ‘y’ - ‘x’.

# Bob was having a hard time doing so, so he asked you to help him find the total number of twin pairs.

def twin_pairs(array):
    
    n=len(array)
    count  =0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if (array[j]-array[i]) == j-i:
                
                count +=1
                
    return count

a=[1 ,1, 4, 3]
print(twin_pairs(a))