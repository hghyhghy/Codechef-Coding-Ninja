#usbarry with given xor 

def main(arr:list[int],target:int)->int:
    
    n=len(arr)
    count  = 0
    
    for i in range(n):
        
        current = 0 
        
        for j in range(i,n):
            
            current ^= arr[j]
            
            if current == target:
                
                count += 1
    
    return count

n,target=map(int,input().split())
arr=list(map(int,input().split()))

print(main(arr,target))
