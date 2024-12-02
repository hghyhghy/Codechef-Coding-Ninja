# Problem statement
# You are given an array ‘ARR’ having ‘N’ integers. You are also given an integer ‘K’. The task is to count the number of subarrays that have ‘K’ distinct values.



# Subarray: A consecutive sequence of one or more values taken from an array.



# For Example :
# ‘N’ = 4, ‘K’ = 2
# ‘ARR’ = [1, 1, 2, 3]

# There are ‘3’ subarrays with ‘2’ distinct elements, which are as follows: [1, 2], [2, 3], [1, 1, 2].
# Thus, you should return ‘3’ as the answer.

def count_subarray_with_k_distinct(array:list[int],k:int)->int:
    
    n =len(array)
    count= 0
    
    for start in range(n):
        
        seen=set()
        
        for end in range(start,n):
            
            seen.add(array[end])
            
            if len(seen) == k:
                
                count += 1
                
            elif len(seen) > k:
                
                break
            
            
    return count

arr = [1, 2, 1, 2, 3]
K = 2
print(count_subarray_with_k_distinct(arr,K))
            
            