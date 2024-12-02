

#subarray sum equal to k

def main(array,k):
    
    n=len(array)
    count=0
    
    for i in range(n):
        
        total = 0
        
        for j in range(i,n):
            
            total += array[j]

            if total == k:
                
                count +=1
                
    return count

nums = [1, 1, 1]
k = 2
print(main(nums,k))