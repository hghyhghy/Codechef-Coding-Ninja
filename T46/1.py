# Problem statement
# You are given an array 'ARR' of the 'N' element. Your task is to find the maximum difference between any of the two elements from 'ARR'.

# If the maximum difference is even print “EVEN” without quotes. If the maximum difference is odd print “ODD” without quotes.

# For example:

# Given 'ARR' = [1, 10, 5, 2, 8, 1 ] , answer is "ODD".
# Here the maximum difference is between 10 and 1, 10 - 1 = 9

def maximum_difference_of_an_array(array):
    
    n=len(array)
    if   n == 1:
        
        return array
    maximum =array[0]
    minimum=array[0]
    
    for num in array[1:]:
        
        if num > maximum:
            
            maximum = num
            
        if num < minimum:
            
            minimum = num
            
    
    difference = maximum - minimum
    
    return difference

arr = [1, 2, 90, 10, 110]
print(maximum_difference_of_an_array(arr))