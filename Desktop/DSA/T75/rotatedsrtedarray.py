# Problem statement
# You have been given an array of ‘N’ distinct integers which is sorted in ascending order and then rotated to the left by an unknown which you don’t know beforehand. For a given integer ‘X’, your task is to find the index of ‘X’ in the given array if it exists.

# Please note that the sorted array A : [2, 3, 6, 8, 9, 11, 15] might become [6, 8, 9, 11, 15, 2, 3] after rotating it twice to the left.

# Detailed explanation ( Input/output format, Notes, Im

def element_in_roated_sorted_array(array:list[int],x:int)->int:
    
    n=len(array)
    left=0
    right=n-1
    
    
    while left<=right:
        
        mid=(left+right)//2
        
        if array[mid] == x:
            return mid
        
        if array[left]<=array[mid]:
            
            if array[left]<=x<array[mid]:
                
                right = mid-1
                
            else:
                
                left=mid+1
                
        else:
            
            if array[mid]<x<=array[right]:
                
                left=mid+1
                
            else:
                
                right=mid-1
                
    return -1

arr = [6, 8, 9, 11, 15, 2, 3]
x = 9
print(element_in_roated_sorted_array(arr,x))