# You are given ‘N’ integers in the form of an array ‘ARR’. Count the number of subarrays having their sum as 0.

# For example :
# Let ‘ARR’ be: [1, 4, -5]
# The subarray [1, 4, -5] has a sum equal to 0. So the count is 1.

def count_subarray_with_zero(array:list[int])->int:
    
    n=len(array)
    count = 0 
    
    for start in range(n):
        
        curr =0 
        
        for end in range(start,n):
            
            curr += array[end]
            
            if curr == 0:
                
                count += 1
                
    return count

arr = [1, -1, 2, -2, 3, -3]
print(count_subarray_with_zero(arr))