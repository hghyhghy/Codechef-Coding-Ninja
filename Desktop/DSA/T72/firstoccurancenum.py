# Problem statement
# You are given an array of integers ‘A’ having ‘N’ number of elements. It is given that all the numbers in the array occur twice except the two numbers that appear only one time. You need to find those two non-repeating numbers.

# For Example:
# If the given array is [ 4, 7, 3, 2, 7, 2 ], you have to find ‘4’ and ‘3’ as 4 and 3 occur one time, and the rest of the elements ( 7 and 2 ) are occurring twice.

def first_non_repeating_number(array:list[int])->list[int]:
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    result=[]
    
    for num,count in freq.items():
        
        if count ==  1:
            
            result.append(num)
            
    return result

arr = [4, 7, 3, 2, 7, 2]
print(first_non_repeating_number(arr))
