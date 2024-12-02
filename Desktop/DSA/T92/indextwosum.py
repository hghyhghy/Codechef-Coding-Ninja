# Problem statement
# Given an integer array Arr of size N and an integer target, your task is to find the indices of two elements of the array such that their sum is equal to target. Return <-1,-1> if no such pair exists.

# Note:

# If more than one such pair of indices exist, return the lexicographically smallest pair
# You may not use the same element twice.

def index_of_two_sum(array:list[int],target:int)->int:
    
    n=len(array)
    result=(-1,-1)

    for i in range(n):
        
        for  j in range(i+1,n):
            
            if array[i]+array[j] == target:
                
                if result==(-1,-1) or (i,j) < result:
                    
                    result=(i,j)

    return result

Arr = [1, 3, 2, 4, 6]
target = 6

print(index_of_two_sum(Arr,target))