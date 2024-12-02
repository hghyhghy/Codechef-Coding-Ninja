# You have been given an array 'A' of N integers. You need to find the maximum value of j - i subjected to the constraint of A[i] <= A[j], where ‘i’ and ‘j’ are the indices of the array.

# For example :
# If 'A' = {3, 5, 4, 1}

# then the output will be 2.
# Maximum value occurs for the pair (3, 4)

def maximum_distance(array:list[int])->int:
    
    n=len(array)
    maximum =float('-inf')
    
    for i in range(n):
        
        for j in range(i,n):
            
            if array[i]<=array[j]:
                
                temp = array[j] - array[i]
                
                if temp > maximum:
                    
                    maximum =  temp
                    
    return maximum

A = [3, 5, 4, 1]
print(maximum_distance(A))