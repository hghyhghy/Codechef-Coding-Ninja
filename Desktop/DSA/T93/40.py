#two sum optimized 

def main(arraty,target):
    
    n=len(arraty)
    left=0
    right=n-1
    
    while left <  right:
        
        current=  arraty[left]+arraty[right]    

        if current==target:
            
            return left,right
        
        if current < target:
            
            left += 1
            
        else:
            
            right -= 1
            
    return -1

n=int(input("enter"))
ar=list(map(int,input().split()))

print(main(ar,n))