# You are given an array 'ARR' of the 'N' element. Your task is to find the maximum difference between any of the two elements from 'ARR'.

# If the maximum difference is even print “EVEN” without quotes. If the maximum difference is odd print “ODD” without quotes.

def maximum_difference_elements(array):
    
    n=len(array)
    max_difference=float("-inf")
    
    array.sort(reverse=True)

    maximum=array[0]

    for i in range(n):
        
        difference = maximum  - array[i]

        if difference > max_difference:
            
            max_difference  = difference
            
            
    return max_difference

a=[1, 10, 5, 2, 8, 1 ]
print(maximum_difference_elements(a))
    