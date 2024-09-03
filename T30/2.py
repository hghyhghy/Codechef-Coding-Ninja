# reverse the first k lements of the array 

def reverse_first_k_elements(arr,k):
    
    if len(arr) < k:
        
        return arr
    
    
    start=0
    end=k-1
    
    while start < end:
        
        arr[start],arr[end] = arr[end],arr[start]
        
        start += 1
        
        end -= 1
        
        
    return arr

arr = [1, 2, 3, 4, 5]
k = 3

print(reverse_first_k_elements(arr,k))