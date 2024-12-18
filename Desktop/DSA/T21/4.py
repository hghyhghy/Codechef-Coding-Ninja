# 189. Rotate Array
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate_array(arr,start,end):
    
    while start <= end:
        
        arr[start],arr[end] = arr[end],arr[start]

        start += 1
        end -=1
        

def main_function(arr,k):
    
    n=len(arr)
    k=k%n
    
    rotate_array(arr,0,n-1)

    rotate_array(arr,0,k-1)

    rotate_array(arr,k,n-1)

    return arr

nums = [1,2,3,4,5,6,7]
k = 3
print(main_function(nums,k))
