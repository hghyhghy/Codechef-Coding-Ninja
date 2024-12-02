
#subarray divisible by k

def main(array,k):
    
    n=len(array)
    count=0
    
    for i in range(n):
        
        curr = 0
        
        for j in range(i,n):
            
            curr += array[j]
            
            if curr % k ==0:
                
                count +=1
                
    return count


arr = [4, 5, 0, -2, -3, 1]
K = 5

print(main(arr,K))