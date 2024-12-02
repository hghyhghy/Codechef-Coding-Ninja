
#subarray with distinct k elements 

def main(arr:list[int],k:int)->int:
    
    n=len(arr)
    count= 0
    
    for start in range(n):
        
        seen=set()

        for end in range(start,n):
            
            seen.add(arr[end])

            if len(seen) == k:
                
                count += 1
                
            elif len(seen) > k:
                
                break
            
    return count

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))