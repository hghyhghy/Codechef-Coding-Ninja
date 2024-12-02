# Problem statement
# Given an array 'arr' with 'n' elements, the task is to rotate the array to the left by 'k' steps, where 'k' is non-negative.



# Example:
# 'arr '= [1,2,3,4,5]
# 'k' = 1  rotated array = [2,3,4,5,1]
# 'k' = 2  rotated array = [3,4,5,1,2]
# 'k' = 3  rotated array = [4,5,1,2,3] and so on.

def rotate(arr,start,end):
    
    while start < end:
        
        arr[start],arr[end]=arr[end],arr[start]
        start += 1
        end -= 1
        
def main_function(arr,k):
    
    n=len(arr)
    k = k%n 
    
    rotate(arr,0,n-1)

    rotate(arr,0,n-k-1)

    rotate(arr,n-k,n-1)
    
    return arr

arr = [1,2,3,4,5]
k=2

print(main_function(arr,k))