# You are given an array arr of N non-negative integers, you need to return true if the array elements consist of consecutive numbers otherwise return false.

# For Example: If the given array is [4,3,5] then you should return true as all the array elements are in consecutive order.

def is_consecutive(array:list[int])->bool:
    
    n=len(array)

    array.sort()

    for i in range(1,n):
        
        if array[i] - array[i-1] != 1:
            
            return False
        
    
    return  True

arr = [4, 3, 5]
print(is_consecutive(arr))