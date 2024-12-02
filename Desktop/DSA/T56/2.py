# You are given a sorted array ARR of integers of size N and an integer K. You have to find whether it is possible to find a pair of integers having an absolute difference of K.

# Note:

# 1. K is a non-negative integer.

# 2. Absolute Difference between two integers A and B is equal to the difference of maximumOf(A, B) and minimumOf(A, B).

# 3. Pair of integers should have different indices in the array.

def pair_with_difference_k(array,target):
    
    left=0
    right=1
    
    n=len(array)
    array.sort()

    while right <  n:
        
        difference  = array[right] - array[left]

        if difference == target:
            
            return True
        
        elif difference < k:
            
            right += 1
            
        else:
            
            left += 1
            
            
            if left == right:
                
                right += 1
                
    return False

arr = [1, 3, 5, 8, 9]
k = 4

print(pair_with_difference_k(arr,k))