# reversing an array without using operator 

def reverse_array_without_operator(arr):
    
    left=0
    right=len(arr) - 1
    
    while  left < right:
        
        arr[left],arr[right] = arr[right],arr[left]

        left += 1
        
        right -= 1
        
        
    return arr

array = [1, 2, 3, 4, 5]
print(reverse_array_without_operator(array))