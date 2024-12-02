# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# # Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

def k_pairs_smallest_sum(array1,array2,k):
    
    result=[]
    
    for i in array1:
        
        for j in array2:
            
            result.append((i,j))

    
    result.sort(key=lambda x : x[0] + x[1])

    return result[:k]

nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3

print(k_pairs_smallest_sum(nums1,nums2,k))