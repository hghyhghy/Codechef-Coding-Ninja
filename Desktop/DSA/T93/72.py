
#maximum sum subarray

def main(array):
    
    n=len(array)
    maximum =float("-inf")

    for i in range(n):
        
        curr= 0
        
        for j in range(i,n):
            
            curr += array[j]

            if curr==0:
                
                length =j-i+1
                
                maximum=max(maximum,length)

    return maximum

array=list(map(int,input().split()))
print(main(array))