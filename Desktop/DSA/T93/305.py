

#maximum average subarry 

def main(array,k):
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n-k+1):
        
        current= 0 
        
        for j in range(i,i+k):
            
            current += array[j]
            
            maximum = max(maximum,current)

    return maximum/k

nums = [1, 12, -5, -6, 50, 3]
k = 4

print(main(nums,k))