# Given an array of integers, print the minimum of the absolute difference of all possible pairs of elements.

# Example :
# N = 5
# ARR = [ 3, -6, 7, -7, 0 ]
# Out of all pairs, (-7,-6) have a difference of ‘1’, and no other pair has less difference. So ‘ANS’ is ‘1’.    

def minimum_difference_of_array(array:list[int])->int:
    
    n=len(array)
    if n <2:
        
        return array
    
    minimum_diff=  float('inf')
    
    for i in range(n):
        
        for j in range(i,n):
            
            difference =  abs(array[i] - array[j])
            
            if difference < minimum_diff:
                
                minimum_diff =  difference
                
    return minimum_diff

arr = [3, -6, 7, -7, 0]
print(minimum_difference_of_array(arr))
    
