

def rotate(arr,start,end):
    
    while start < end:
        
        arr[start],arr[end]=arr[end],arr[start]

        start +=1
        end -=1
        

def main(arr,k):
    
    n=len(arr)

    k=k%n
    
    rotate(arr,0,k-1)

    rotate(arr,k,n-1)
    
    rotate(arr,0,n-1)

    return arr

k=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,k))
    
    