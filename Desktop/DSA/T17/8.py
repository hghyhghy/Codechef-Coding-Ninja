# Given two integer arrays nums1 and nums2, return an array of their 
# intersection
# . Each element in the result must be unique and you may return the result in any order.

def intersection(a1,a2):
    
    t1=set(a1)
    t2=set(a2)

    result= t1 & t2
    
    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1,nums2))
