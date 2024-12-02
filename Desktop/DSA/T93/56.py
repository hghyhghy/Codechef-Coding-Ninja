
#maximum of all subarray of size k 

def main(array,k):
    
    n=len(array)
    r=[]

    for i in range(n-k+1):
        
        maximum=array[i]

        for j in range(i,i+k):
            
            if array[j]>maximum:
                
                maximum =  array[j]

        
        r.append(maximum)

    
    return r

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))