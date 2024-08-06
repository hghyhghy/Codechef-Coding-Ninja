# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).search an element in this array return tru if found else return false

def searching_element_in_an_array(arry,target):
    
    left=0
    right=len(arry) - 1
    
    while left <= right:
        
        mid=(left+right)//2 
        
        if arry[mid] == target:
            
            return True
        
        elif arry[mid]< target:
            
            left = mid+1
            
        else:
            
            right = mid-1
            
    return False

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

print(searching_element_in_an_array(nums,target))