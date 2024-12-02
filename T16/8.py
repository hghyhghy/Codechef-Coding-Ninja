# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

def kth_largest_elements(arr,k):
    
    def quick_sort(arr):
        
        if len(arr) <= 1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            
            left=[x for x in arr if x > mid]
            middle=[x for x in arr if x == mid]
            right=[x for x in arr if x < mid]

            return quick_sort(left) + middle + quick_sort(right)

    temp=quick_sort(arr)
    return temp[k-1]

nums = [3,2,1,5,6,4]
k = 2
print(kth_largest_elements(nums,k))
