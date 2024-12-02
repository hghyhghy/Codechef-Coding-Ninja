

#circular subarray 

def main(array):
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n):
        
        curr=0
        
        for j in range(i,i+n):
            
            curr += array[j%n]
            
            maximum=max(maximum,curr)
            if curr < 0:
                
                curr=0

    
    return maximum

arr = [1, 2, -3, -4, 5]
print(main(arr))