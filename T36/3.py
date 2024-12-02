# Given an array of integers, find the Kth largest sum subarray For example, given the array [1, -2, 3, -4, 5] and K = 2, the 2nd largest sum subarray would be [3, -4, 5], which has a sum of 4.

# Please note that a subarray is the sequence of consecutive elements of the array.

def largest_subarry_sum(array):
    
    n=len(array)
    max_sum=float('-inf')

    for start  in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            max_sum=max(max_sum,current_sum)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(largest_subarry_sum(arr))