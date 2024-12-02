# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

def next_greater_element(array):
    
    n=len(array)
    dp =[-1]*n
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j] > array[i]:
                
                dp[i]= array[j]
                break
            
    return dp

nums = [1, 2, 1]
print(next_greater_element(nums))