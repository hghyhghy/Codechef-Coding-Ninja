# 373. Find K Pairs with Smallest Sums
# Medium
# Topics
# Companies
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 
def kth_pair_with_smallest_sum(a1,a2,k):
    
    if not a1 or not a2 or k<=0:
        
        return None
    
    pair=[]

    for num in a1:
        
        for num1 in a2:
            
            pair.append([num,num1])

    
    pair.sort(key=lambda x: x[0] + x[1])

    return pair[:k]

nums1 = [1, 7]
nums2 = [3, 5]
k = 3

print(kth_pair_with_smallest_sum(nums1,nums2,k))

