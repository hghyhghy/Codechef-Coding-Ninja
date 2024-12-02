

#subarray equal to sum k 

def main(array,k):
    
    n=len(array)
    count = 0
    
    for start in range(n):
        
        current = 0
        
        for end in range(start,n):
            
            current += array[end]

            if current == k:
                
                count +=1
                
    return count


nums = [1,1,1]
k = 2

print(main(nums,k))