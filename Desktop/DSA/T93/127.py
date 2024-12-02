

#minimum subarray sum

def main(array:list[int],target:int)->int:

    n=len(array)
    minimum=float("inf")

    for i in range(n):
        
        curr = 0 
        
        for j in range(i,n):
            
            curr += array[j]

            if curr >= target:
                
                minimum = min(minimum,j-i+1)
                
                break
            
    return minimum

n=int(input("enter"))
nums=list(map(int,input().split()))

print(main(nums,n))
    
    