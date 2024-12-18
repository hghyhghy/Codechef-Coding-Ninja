
#search in the rotated sorted array

def main(array,target):
    
    n=len(array)
    left=0
    right=n-1
    
    while left<=right:
        
        mid=(left+right)//2
        
        if array[mid] == target:
            
            return mid
        
        if array[left]<=array[mid]:
            
            if array[left]<=target<array[mid]:
                
                right = mid-1
                
            else:
                
                left= mid+1
                
            
        else:
            
            if array[mid]<target<=array[right]:
                
                left =mid+1
                
            else:
                
                right=mid-1
                
    return -1

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))