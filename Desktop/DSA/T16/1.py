# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 
def peak_element_of_the_array(array):
    
    peak_element= array[0]

    for i in range(len(array)-1):
        
        if array[i] > peak_element:
            
            peak_element =  array[i]

    return i

nums = [1,2,3,1]
print(peak_element_of_the_array(nums))