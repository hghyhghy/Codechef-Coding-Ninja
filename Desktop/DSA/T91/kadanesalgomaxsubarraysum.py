# Problem statement
# You are given an array/list ARR consisting of N integers. Your task is to find the maximum possible sum of a non-empty subarray(contagious) of this array.

# Note: An array C is a subarray of array D if it can be obtained by deletion of several elements(possibly zero) from the beginning and the end of array D.

# For e.g.- All the non-empty subarrays of array [1,2,3] are [1], [2], [3], [1,2], [2,3], [1,2,3].

def kadanes_algorithm(array:list[int])->int:
    
    total_sum=0
    max_sum=float("-inf")

    for num in array:
        
        total_sum += num

        if total_sum > max_sum:
            
            max_sum = total_sum
            
        if total_sum < 0:
            
            total_sum = 0
            
    return max_sum

ARR = [1, 2, -3, 4, 5]
print(kadanes_algorithm(ARR))