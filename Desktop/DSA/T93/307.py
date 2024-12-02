


#binary search 

def main(arry,target):
    
    n=len(arry)
    left=0
    right=n-1
    
    while left <= right:
        
        mid= (left+right)//2
        
        if arry[mid] == target:
            
            return mid
        
        elif arry[mid] < target:
            
            left +=1
            
        else:
            
            right -=1
            
    return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

print(main(nums,target))