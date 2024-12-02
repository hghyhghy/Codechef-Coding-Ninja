
#minimum subarray

def main(arr:list[int],target:int)->int:
    
    n=len(arr)
    minimum=float("inf")

    for i in range(n):
        
        current=0
        
        for j in range(i,n):
            
            current += arr[j]

            if current > target:
                
                minimum = min(minimum,j-i+1)
                
                break
            
    
    return minimum

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))