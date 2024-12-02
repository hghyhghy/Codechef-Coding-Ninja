# Problem statement
# Given an array 'arr' with 'n' elements, the task is to rotate the array to the left by 'k' steps, where 'k' is non-negative.



# Example:
# 'arr '= [1,2,3,4,5]
# 'k' = 1  rotated array = [2,3,4,5,1]
# 'k' = 2  rotated array = [3,4,5,1,2]
# 'k' = 3  rotated array = [4,5,1,2,3] and so on.
# Detailed explanation ( Input/output format, Notes, Im

def reverse(arr,start,end):
    
    while start<end:
        
        arr[start],arr[end] =  arr[end],arr[start]
        
        start += 1
        
        end -= 1
        

def rotation_main(arr,k):
    
    n=len(arr)

    k= k%n
    
    reverse(arr,0,k-1)
    
    reverse(arr,k,n-1)
    
    reverse(arr,0,n-1)
    
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(rotation_main(arr,k))