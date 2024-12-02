# Problem statement
# Given an array 'arr' with 'n' elements, the task is to rotate the array to the left by 'k' steps, where 'k' is non-negative.

def function(arr,start,end):
    
    while start < end:
        
        arr[start],arr[end]= arr[end],arr[start]
        
        start += 1
        end -= 1
        

def main(arr,k):
    
    n=len(arr)
    k=k%n
    
    function(arr,0,n-1)
    
    function(arr,0,n-k-1)

    function(arr,k-1,n-1)

    return arr

arr=[1,2,3,4,5]
k=3

print(main(arr,k))
