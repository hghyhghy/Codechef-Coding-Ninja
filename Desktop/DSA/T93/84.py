
#chocolate distribution 

def main(array,m):

    n=len(array)

    if n==0 or m==0:
        
        return 0
    
    arr.sort()
    minimum=float("inf")

    for i in range(n-m+1):
        
        difference =  array[i+m-1] -  array[i]

        minimum = min(minimum,difference)

    
    return minimum

m=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,m))

    
    