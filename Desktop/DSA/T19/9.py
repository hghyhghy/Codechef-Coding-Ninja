# 912. Sort an Array
# Medium
# Topics
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

def sorted_array(array):
    
    if len(array) <=1 :
        
        return array
    
    else:
        
        mid=array[len(array)// 2]
        left =[ x for x in array if x < mid]
        middle=[ x for x in array if x == mid]
        right=[ x for x in array if x > mid]

        return sorted_array(left) + middle + sorted_array(right)

nums = [5,2,3,1]
print(sorted_array(nums))