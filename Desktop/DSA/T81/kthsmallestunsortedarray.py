
# Contributed by
# 23 upvotes
# Asked in companies
# Problem statement
# Given an unsorted array ‘arr’ of distinct integers and an integer ‘k’, your task is to find the ‘k-th’ smallest element in the array.

# Example:
# n = 5, k = 2 and arr[] = {6, 5, 4, 8, 7}
# The array elements in sorted order are [4, 5, 6, 7, 8]. The ‘2-nd’ smallest element in the array is 5, so the answer is 5.
# Note:
# 1. Don’t print anything. Return the value of ‘k-th’ smallest element.
# 2. ‘k’ is a positive integer and not greater than the size of the array.
# 3. The array ‘arr’ is unsorted, and all the elements of the array are distinct.


def bubble_sort(array:list[int])->list[int]:
    
    n=len(array)
    
    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j] > array[j+1]:
                
                array[j],array[j+1] = array[j+1],array[j]
                
    return array

def main(array:list[int],k:int)->int:
    
    temp_array =  bubble_sort(array)
    
    return temp_array [k-1]

arr = [6, 5, 4, 8, 7]
k = 2
print(main(arr,k))