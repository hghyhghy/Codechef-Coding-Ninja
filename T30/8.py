# Problem statement
# You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

# Note:
# a) Duplicate elements may be present.

# b) If no such element is present return -1.
# Example:
# Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

def second_largestelement_from_the_array(arr):
    
    def quick_sort(arr):
        
        if len(arr) <= 1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x > mid]
            middle=[x for x in arr if x == mid]
            right=[x for x in arr if x < mid]

            return quick_sort(left) + middle+ quick_sort(right)

    
    temp= quick_sort(arr)

    return temp[1]

a=[2, 4, 5, 6, 8.]
print(second_largestelement_from_the_array(a))