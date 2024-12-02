#subarray with given sum

def main(arr,target):
    
    n=len(arr)

    for i in range(n):
        
        current =0
        
        for j in range(i,n):
            
            current += arr[j]

            if current == target:
                
                return [i,j]

    return [-1,-1]
n,target=map(int,input().split())
arr=list(map(int,input().split()))

print(main(arr,target))