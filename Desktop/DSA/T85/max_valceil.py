# Problem statement
# You are given an array, 'ARR', consisting of ‘N’ integers. You are also given two other integers, ‘SUM’ and ‘MAXVAL’. The elements of this array follow a special property that the absolute value of each element is not more than ‘MAXVAL’.

# Your task is to determine the minimum number of integers required to be added into the array such that the sum of all the elements of the array becomes equal to ‘SUM’.

# Note:
# All the new numbers being added to the array must follow the original property of the array.

import math

def min_integer_to_add(array:list[int],target:int,max_val:int):
    
    current  = sum(array)

    difference= abs(target - current)

    if difference == 0:
        
        return  0
    
    minimum_integer =  math.ceil(difference/max_val)

    return minimum_integer


arr = [1, -2, 3]  # Example array
target_sum = 10   # Target sum
maxval = 5        # Maximum absolute value that can be added

# Find the minimum number of integers to add
result = min_integer_to_add(arr, target_sum, maxval)
print(result)