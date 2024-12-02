# Problem statement
# Given an array 'A' consisting of 'N' integers, find the smallest subarray of 'A' containing exactly 'K' distinct integers.

# Note :
# If more than one such contiguous subarrays exist, consider the subarray having the smallest leftmost index.

# For example - if A is [1, 2, 2, 3, 1, 3 ] and k = 2 then the subarrays: [1,2], [2,3], [3,1], [1,3] are the smallest subarrays containing 2 distinct elements. In this case, we will consider the starting and ending index of subarray [1,2] i.e. 0 and 1

def smallest_subarray_with_distinct_elements(arr):
    
    n=len(arr)
    lenght=0
    
    for start in range(n):
        
        store=set()

        for end in range(start,n):
            
            store.add(arr[end])

            
            if len(store) == (end-start+1):
                
                lenght=min(lenght,end-start+1)

    return lenght

arr = [1, 2, 3, 2, 4, 5, 3]
print(smallest_subarray_with_distinct_elements(arr))