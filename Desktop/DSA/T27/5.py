# You are given an array 'ARR' of integers of length N. Your task is to find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can have negative numbers as well.

# For example, the input [3, 4, -1, 1] should give output 2 because it is the smallest positive number that is missing in the input array.


def first_common_missing_element(arr):
    
    positive=set()

    for num in arr:
        
        if num > 0:
            
            positive.add(num)

    
    missing=1
    
    while missing in positive:
        
        missing += 1
        
    return missing

arr = [3, 4, -1, 1]
print(first_common_missing_element(arr))