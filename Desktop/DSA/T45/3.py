# You are given an array ‘ARR’ of size ‘N’ and an integer ‘M’. You have to split the array into ‘M’ non-overlapping, non-empty subarrays such that the maximum of all the subarray’s sum is the minimum possible. Your task is to return the minimum of the maximum of all the subarray’s sum.

# For example:
# You are given ‘ARR’ = [7, 2, 6, 10, 8] and ‘M’ = 2. We split the array as [ 7, 2, 6] and [10, 8], the maximum of 7 + 2 + 6  and 10 + 8 is 18, which is the minimum possible.

def splitting_the_array(array,m):
    
    if len(array) < m:
        
        return array
    
    part1=array[:m]
    part2=array[m:]

    return part1,part2


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
M = 4
print(splitting_the_array(arr,M))