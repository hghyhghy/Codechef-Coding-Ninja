

#search using binary search 

def main(array,target):
    
    n=len(array)
    left=0
    right=n-1
    
    
    while left<=right:
        
        mid=(left+right)//2
        
        if array[mid] == target:
            
            return mid
        
        elif array[mid] <target:
            
            left = mid+1
            
        else:
            
            right=mid-1
            
    return -1

arr = [1, 2, 4, 5, 7, 8, 10, 12, 14]
target = 7

print(main(arr,target))