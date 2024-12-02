
#difference with pair

def main(array,target):
    
    n=len(array)
    left=0
    right=1
    
    while right<n:
        
        difference=array[right]-array[left]
        
        if difference == target:
            
            return True
        
        elif difference <target:
            
            right +=1
            
        else:
            
            left +=1
            
        
        if left==right:
            
            right +=1
            
    return False

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))