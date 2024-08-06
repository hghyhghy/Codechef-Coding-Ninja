# Count Subarray sum Equals K

def subarray_with_given_sum(array,target):
    
    n=len(array)
    count= 0 
    
    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum ==  target:
                
                count += 1
                
                
    return count

arr = [1, 2, 3, 4, 2]
k = 5
print(subarray_with_given_sum(arr,k))