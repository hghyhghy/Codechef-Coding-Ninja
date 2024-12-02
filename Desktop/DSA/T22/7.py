# 912. Sort an Array
# Medium
# Topics
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

def sorting_arry_using_bubble_sort(array):

    n=len(array)

    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j] > array[j+1]:
                
                array[j],array[j+1] = array[j+1],array[j]            

    return array

nums = [5,2,3,1]
print(sorting_arry_using_bubble_sort(nums))
            