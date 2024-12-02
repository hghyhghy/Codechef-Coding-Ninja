# Problem statement
# Given an array ‘A’ of size ‘N’, sorted in non-decreasing order. Return the pair of two distinct indices whose value adds up to the given ‘target’. The given array is 0 indexed. So returned indices are in the range [0, N-1], both inclusive. If there are multiple answers, you can return any.

# For example:
# Suppose ‘N’ = 5, ‘A’ = [1,2,3,4,5], and target = 8
# As target == A[2] + A[4] = 3 + 5 = 8.
# Hence output will be 2 4.

def two_sum(array:list[int],target:int)->int:
    
    left=0
    right = len(array)-1
    
    while left < right:
        
        current  =  array[left]+array[right]

        if current ==  target:
            
            return left,right
        
        elif current < target:
            
            left +=1 
            
        else:
            
            right -= 1
            
    return -1


arr = [1, 2, 3, 4, 5]
target = 8
print(two_sum(arr,target))