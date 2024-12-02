# You have been given an array/list ‘ARR’ consists of positive integers. We call a contiguous subarray of ‘ARR’ good if the number of different integers in that subarray is exactly ‘K’. Your task is to find out the number of good subarrays of ‘ARR’.

# For example:

# ‘ARR[]’ = [1, 3, 1, 1, 2] has 3 different integers: 1, 2, and 3. And for ‘K’ = 2, following are the good subarrays.
# 1. [1, 3]
# 2. [1, 3, 1]
# 3. [1, 3, 1, 1]
# 4. [3, 1]
# 5. [3, 1, 1]
# 6. [1, 1, 2]
# 7. [1, 2]

def count_of_good_subarray(array:list[int],k:int)->int:
    
    n=len(array)
    count = 0
    
    for i in range(n):
        
        seen=set()
        
        for j in range(i,n):
            
            seen.add(array[j])

            if len(seen)  == k:
                
                count += 1
                
            elif len(seen) > k:
                
                break
            
    return count

arr = [1, 3, 1, 1, 2]
k = 2
print(count_of_good_subarray(arr,k))