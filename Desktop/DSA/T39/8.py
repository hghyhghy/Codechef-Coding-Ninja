# Problem statement
# Given an array with N elements, the task is to reverse all the array elements and print the reversed array.

def reverse_array_using_pointers(array):
    
    n=len(array)
    left = 0
    right=n-1
    
    while  left < right:
        
        array[left],array[right] =  array[right],array[left]

        left += 1
        right -= 1
        
        
    return  array

arr = [1, 2, 3, 4, 5]
print(reverse_array_using_pointers(arr))