# You are given an array arr consisting of ‘N’ integers. Your task is to find the largest number, ‘K’, such that both the values ‘K’ and -‘K’ are present in the given array 'arr'. If no such number exists, then return '-1'.

# For example:
# Consider ‘arr’ = [1,2,-2,-1], the largest value of ‘K’ is 2, since a negative of 2 is also present in the array. Hence, the answer is 2.

def maximum_element_from_array(array):
    
    n=len(array)
    maximum = array[0]

    for i in range(n):
        
        if array[i] > maximum:
            
            maximum =  array[i]

    return maximum

a=[1,2,-2,-1]
print(maximum_element_from_array(a))