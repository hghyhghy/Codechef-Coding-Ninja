# You have given a sorted array 'A' of 'N' integers.

# Now, you are given 'Q' queries, and each query consists of a single integer 'X'. Your task is to check whether 'X' is present in array 'A' or not for each query. If 'X' exists in array 'A', you need to print 1 else print 0.

# Note :

def binary_search_element(array:list[int],target:int)->int:
    
    n=len(array)
    left=0
    right=n-1
    
    while left<=right:
        
        mid=(left+right)//2
        
        if array[mid] ==  target:
            
            return 1
        
        elif array[mid]<target:
            
            left=mid+1
            
        else:
            
            right=mid+1
            
    return 0

a=[1 ,2 ,3 ,4 ,5]
print(binary_search_element(a,4))