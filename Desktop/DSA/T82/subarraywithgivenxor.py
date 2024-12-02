# Problem statement
# Given an array of integers ‘ARR’ and an integer ‘X’, you are supposed to find the number of subarrays of 'ARR' which have bitwise XOR of the elements equal to 'X'.

# Note:
# An array ‘B’ is a subarray of an array ‘A’ if ‘B’ that can be obtained by deletion of, several elements(possibly none) from the start of ‘A’ and several elements(possibly none) from the end of ‘A’. 

def count_subarray_with_given_xor(array:list[int],target:int)->int:
    
    n=len(array)
    count = 0
    
    for i in range(n):
        
        current = 0
        
        for j in range(i,n):
            
            current ^= array[j]
            
            if current == target:
                
                count += 1
                
    return count

arr = [1, 2, 3, 4]
X = 3
print(count_subarray_with_given_xor(arr,X))