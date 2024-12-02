# Given two integer arrays nums1 and nums2, return an array of their 
# intersection
# . Each element in the result must be unique and you may return the result in any order.

def intersection_of_two_list(l1,l2):
    
    first=set(l1)
    second=set(l2)

    final = first.intersection(second)

    return list(final)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection_of_two_list(nums1,nums2))
