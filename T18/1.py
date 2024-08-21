
# Code


# Testcase
# Test Result
# Test Result
# 414. Third Maximum Number
# Easy
# Topics
# Companies
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 
def the_third_largest_element(array):
    
    distinct_elements=set(array)

    temp=sorted(distinct_elements,reverse=True)

    if len(temp) >= 3:
        
        return temp[2]

    else:
        
        return temp[0]


nums=[2,2,3,1]
print(the_third_largest_element(nums))