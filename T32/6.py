# Given an unsorted array of integers, you have to move the array elements in a way such that all the zeroes are transferred to the end, and all the non-zero elements are moved to the front. The non-zero elements must be ordered in their order of appearance.

# For example, if the input array is: [0, 1, -2, 3, 4, 0, 5, -27, 9, 0], then the output array must be:

# [1, -2, 3, 4, 5, -27, 9, 0, 0, 0].

# Expected Complexity: Try doing it in O(n) time complexity and O(1) space complexity. Here, ‘n’ is the size of the array.

def move_all_zer_to_the_end(array):
    
    n=len(array)

    j=0
    
    for i in range(n):
        
        if array[i] !=0:
            
            array[j] ,array[i] = array[i],array[j]
            j += 1
            
    return  array

a=[0, 1, -2, 3, 4, 0, 5, -27, 9, 0]
print(move_all_zer_to_the_end(a))
