# Problem statement
# Given an array 'A' consisting of 'N' integers, find the smallest subarray of 'A' containing exactly 'K' distinct integers.

# Note :
# If more than one such contiguous subarrays exist, consider the subarray having the smallest leftmost index.

# For example - if A is [1, 2, 2, 3, 1, 3 ] and k = 2 then the subarrays: [1,2], [2,3], [3,1], [1,3] are the smallest subarrays containing 2 distinct elements. In this case, we will consider the starting and ending index of subarray [1,2] i.e. 0 and 1.

def smallest_subarray_with_k_distinct_elements(array:list[int],k:int)->int:
    
    n=len(array)
    first = -1
    last=-1
    
    minimum = float("inf")
    
    for start in range(n):
        
        seen=set()
        
        for end in range(start,n):
            
            seen.add(array[end])
            
            if len(seen) == k:
                
                length = end-start+1
                
                if length < minimum:
                    
                    first=start
                    last=end
                    minimum =  length
                    
                break
    
    if minimum == float("inf"):
        
        return []
    
    else:
        
        return array[first:last+1]

arr = [1, 2, 2, 3, 1, 3]
K = 2
print(smallest_subarray_with_k_distinct_elements(arr,K))                    