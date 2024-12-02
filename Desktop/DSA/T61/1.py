# Problem statement
# Given an array ‘arr’ of size ‘n’ find the largest element in the array.



# Example:

# Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

# Output: 5

# Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.

def largest_element_in_the_array(array):
    
    def quick_sort(arr):
        
        if len(arr) <=1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            
            left=[x for x in arr  if x >mid]
            middle=[x for x in arr if x == mid]
            right=[ x for x in arr if x <mid]
            
            return quick_sort(left)+middle+quick_sort(right)

    temp=quick_sort(array)

    return temp[0]

a =[1, 2, 3, 4, 5]
print(largest_element_in_the_array(a))