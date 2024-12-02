

#search of an element

def main(array,target):
    
    n=len(array)
    left=0
    right=n-1
    
    while left<=right:

        mid=(left+right)//2

        if array[mid] == target:
            
            return mid
        
        elif array[mid] < target:
            
            left +=1
            
        else:
            
            right-=1
            
    return -1


arr = [1, 3, 5, 7, 9, 11]
target = 7

print(main(arr,target))
        
        
        