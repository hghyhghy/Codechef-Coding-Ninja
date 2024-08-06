# 454. 4Sum II
# Medium
# Topics
# Companies
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

def four_sum_latest(array):
    
    n=len(array)
    store=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                for l in range(k+1,n):
                    
                    if(array[i]+array[j]+array[k]+array[l]) == 0:
                        
                        store.append([array[i],array[j],array[k],array[l]])

    return store

nums = [1, 0, -1, 0, -2, 2]
print(four_sum_latest(nums))