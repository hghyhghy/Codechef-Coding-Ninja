# Problem statement
# You are given an array arr of N non-negative integers, you need to return true if the array elements consist of consecutive numbers otherwise return false.

# For Example: If the given array is [4,3,5] then you should return true as all the array elements are in consecutive order.

def has_consecutive(array):
    
    n=len(array)
    if not array:
        
        return None
    
    for i in range(1,n+1):
        
        if array[i]!= array[i-1]+1:
            
            return False
        
    return True

arr = [3, 4, 5, 6, 7]
print(has_consecutive(arr))