
#binary search 

def main(array,target):
    
    left=0
    right=len(array)-1
    
    while left < right:
        
        mid=(left+right)//2
        
        if array[mid] == target:
            
            return mid
        
        elif array[mid] < target:
            
            left +=1
            
        else:
            
            right -=1
            
    
    return None

arr = [1, 3, 5, 7, 9, 11]
target = 7

print(main(arr,target))