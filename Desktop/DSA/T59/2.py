# You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:

# Select an element m from nums.
# Remove the selected element m from the array.
# Add a new element with a value of m + 1 to the array.
# Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.

def max_count(array,k):
    
    count= 0
    
    for _ in range(k):
        
        max_number=max(array)
        
        index=array.index(max_number)

        count += max_number
        
        array[index] = max_number+1
        
    
    return count

nums = [1, 2, 3, 4, 5]
k=3
print(max_count(nums,k))
        
