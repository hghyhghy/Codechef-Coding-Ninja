
#search using binary search tree

def main(array,target):
    
    n=len(array)
    left=0
    right=n-1
    
    while left <=right:
        
        mid=(left+right)//2
        
        if array[mid] ==  target:
            
            return True
        
        if array[mid]<target:
            
            left = mid+1
            
        else:
            
            right = mid-1
            
    return False

n=int(input("enter"))
array=list(map(int,input().split()))

print(main(array,n))

