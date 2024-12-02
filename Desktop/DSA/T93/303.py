

#subarray divisible by k

def main(array,k):
    
    count=0
    n=len(array)

    for i in range(n):
        
        curr=0
        
        for j in range(i,n):
            
            curr += array[j]

            if curr % k == 0:
                
                count +=1
                
    return count

