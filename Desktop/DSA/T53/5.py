# You are given a sorted array ARR of integers of size N and an integer K. You have to find whether it is possible to find a pair of integers having an absolute difference of K.

# Note:

# 1. K is a non-negative integer.

# 2. Absolute Difference between two integers A and B is equal to the difference of maximumOf(A, B) and minimumOf(A, B).

# 3. Pair of integers should have different indices in the array.

def pair_with_diff_k(array,target):
    
    n=len(array)
    result=[]
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if abs(array[i]-array[j] )== target:
                
                result.append([array[i],array[j]])
    
    return result

arr = [1, 5, 3, 4, 2]
k=3
print(pair_with_diff_k(arr,k))