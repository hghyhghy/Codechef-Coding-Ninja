
#first  and last position of an element

def  main(array,target):
    
    n=len(array)
    first=-1
    last=-1
    
    
    for i in range(n):
        
        if array[i] == target:
            
            first = i
            break
        
    
    
    for j in range(n-1,-1,-1):
        
        if array[j] == target:
            
            last=j
            break
        
    
    return first,last

a=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,a))