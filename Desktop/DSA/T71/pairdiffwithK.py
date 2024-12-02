# Problem statement
# You are given a sorted array ARR of integers of size N and an integer K. You have to find whether it is possible to find a pair of integers having an absolute difference of K.

# Note:

# 1. K is a non-negative integer.

# 2. Absolute Difference between two integers A and B is equal to the difference of maximumOf(A, B) and minimumOf(A, B).

# 3. Pair of integers should have different indices in the array.

def has_pair_with_difference(array:list[int],target:int)->bool:
    
    left=0
    right=1
    
    while  right<len(array):
        
        diff=array[right]-array[left]
        
        if diff == target:
            
            return True
        
        elif diff < target:
            
            right += 1
            
        else:
            
            left += 1
            
            
        if left ==right:
            
            right += 1
    
    return False

arr = [1, 2, 3, 4, 5]
K = 3
print(has_pair_with_difference(arr,K))