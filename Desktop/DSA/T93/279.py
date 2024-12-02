

#shortest subarray with 
def main(array,k):
    
    n=len(array)
    minimum=float("inf")

    for i in range(n):
        
        curr= 0
        
        for j in range(i,n):
            
            curr += array[j]

            if curr >=k:
                
                minimum=min(minimum,j-i+1)

                break
            
    return minimum

