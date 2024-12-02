
#reverse using pointers 

def main(array):
    
    n=len(array)
    left=0
    right=n-1
    
    
    while left  < right:
        
        array[left],array[right]= array[right],array[left]

        left +=1
        right -=1
        
    return array

nums=list(map(int,input().split()))
print(main(nums))
        