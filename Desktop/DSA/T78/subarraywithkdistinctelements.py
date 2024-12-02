# You are given an array/list 'ARR' consisting of 'N' integers and an integer 'B'. A non-empty subarray of 'ARR' is good if it contains exactly 'B' distinct integers.

# Your task is to return the number of good subarrays in the given array/list.

# Example:

# For 'ARR' = [1, 2, 1, 3, 2, 4] and 'B' = 3, one of the good subarrays which contains three distinct integers is [1, 2, 1, 3]. 
# Note:

# An array 'C' is a subarray of array 'D' if it can be obtained by deletion of several elements(possibly zero) from the beginning and the end from array 'D'.

def count_subarrays(array:list[int],k:int)->int:
    
    n=len(array)
    count = 0
    
    for start in  range(n):
        
        seen=set()
        
        for  end in range(start,n):
            
            seen.add(array[end])
            
            if len(seen) == k:
                
                count += 1
                
                
            elif len(seen) > k:
                
                break
            
    return count

arr = [1, 2, 1, 3, 2, 4]
B = 3
print(count_subarrays(arr,B))