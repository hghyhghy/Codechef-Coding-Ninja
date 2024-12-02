# An array ‘A’ of ‘N’ integers is provided. Return the maximum possible number which can be created by taking bitwise XOR of any 2 integers of the array.



# Example:
# If the array is 2,5 and 6

# 2 XOR 5 is 7
# 2 XOR 6 is 4
# 5 XOR 6 is 3

# Hence the answer is 7.

def maximum_xor_of_element(array:list[int])->int:
    
    n=len(array)
    max_xor = 0 
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            xor =  array[i]^array[j]

            max_xor = max(max_xor,xor)

    return max_xor

arr = [2, 5, 6]
print(maximum_xor_of_element(arr))