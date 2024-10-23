# Problem statement
# Given an array with N elements, the task is to reverse all the array elements and print the reversed array.

def reverse_using_pointers(array):
    
    if not array or len(array) <=1:
        
        return array
    
    n=len(array)
    left= 0
    right=n-1
    
    while left < right:
        
        array[left],array[right] =  array[right],array[left]

        left += 1
        right -= 1
        
    return array

a=[7, 5, 2 ,11, 2, 43, 1, 10]
print(reverse_using_pointers(a))