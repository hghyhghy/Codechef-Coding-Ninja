# Search an element in an array

def search_an_element_in_the_array(arr,target):
    
    left=0
    right=len(arr)-1
    
    while left <= right:
        
        mid=(left+right)//2
        
        if arr[mid] == target:
            
            return mid
        
        elif arr[mid] < target:
            
            left = mid + 1
            
        else:
            
            right =mid-1
            
    
    return -1

arr = [1, 3, 5, 7, 9, 11]
target = 7

print(search_an_element_in_the_array(arr,target))

        