# Problem statement
# You are given two lists (array) (nums) of the same size. Your task is to maximise the possible sum which can be calculated using the elements of the two given lists. In order to maximise the sum, you are only allowed to swap any element of the first list (array) with the other that too for any position (any index ‘i’) any number of times.

# Note:
# The maximum sum is calculated by using the following rules:-

def maximizing_sum(arr1,arr2):
    
    n=len(arr1)
    arr1.sort()
    arr2.sort(reverse=True)

    i=0
    j=0
    
    while i<n and j<n:
        
        if arr2[j] > arr1[i]:
            
            arr1[i]=arr2[j]

            i += 1
            
        j += 1
        
    return sum(arr1)

nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]

print(maximizing_sum(nums1,nums2))