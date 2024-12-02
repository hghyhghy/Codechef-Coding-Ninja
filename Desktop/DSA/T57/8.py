# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

import heapq

def kth_largest_element(array,k):
    
    extracted=array[:k]
    heapq.heapify(extracted)

    for num in array[k:]:
        
        if num > extracted[0]:
            
            heapq.heappop(extracted)
            heapq.heappush(extracted,num)

    return extracted[0]

nums = [3, 2, 1, 5, 6, 4]
k = 2

print(kth_largest_element(nums,k))