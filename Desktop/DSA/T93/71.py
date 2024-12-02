
#maximum from subarray of size k 

def main(array,k):
    
    n=len(array)
    result=[]

    for i in range(n-k+1):
        
        subarray = array[i:i+k]
        
        maximum = max(subarray)

        result.append(maximum)

    
    return result

n=int(input("enter a number"))
arr=list(map(int,input().split()))

print(main(arr,n))
