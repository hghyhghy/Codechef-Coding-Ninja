# You are given an integer array 'A' of size 'N', sorted in non-decreasing order. You are also given an integer 'target'. Your task is to write a function to search for 'target' in the array 'A'. If it exists, return its index in 0-based indexing. If 'target' is not present in the array 'A', return -1.

def main_binary_search(array,target):
    
    n=len(array)
    left=0
    right=n-1
    
    while left<=right:
        
        mid=(left+right)//2
        
        if array[mid] == target:
            
            return mid
        
        elif array[mid]<target:
            
            left =mid+1
            
        else:
            
            right=mid-1
            
    return -1

A = [1, 2, 4, 5, 6, 8, 9]
target = 5

print(main_binary_search(A,target))

