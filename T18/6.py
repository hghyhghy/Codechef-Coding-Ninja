# 540. Single Element in a Sorted Array
# Medium
# Topics
# Companies
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

def single_element_in_sorted_array(array):
    
    count={}

    for num in array:
        
        if num in count:
            
            count[num] += 1
            
        else:
            
            count[num] = 1
    
    single_elemwnt =[num for num,freq in count.items() if freq == 1]

    return single_elemwnt

nums = [1,1,2,3,3,4,4,8,8]
print(single_element_in_sorted_array(nums))