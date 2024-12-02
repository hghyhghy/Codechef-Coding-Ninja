# You have given a sorted array 'A' of 'N' integers.

# Now, you are given 'Q' queries, and each query consists of a single integer 'X'. Your task is to check whether 'X' is present in array 'A' or not for each query. If 'X' exists in array 'A', you need to print 1 else print 0.

# Note :

# The given array is sorted in non-decreasing order. 

def search_using_binary_search(array,target):
    
    n=len(array)
    left= 0
    right=n-1

    while left <=right:
        
        mid=(left+right)//2
        
        if array[mid] ==  target:
            
            return mid
        
        elif array[mid]< target:
            
            left = mid+1
            
        else:
            
            right=mid-1
            
    return -1

arr = [1, 2, 4, 5, 7, 8, 10, 12, 14]
target = 7

print(search_using_binary_search(arr,target))