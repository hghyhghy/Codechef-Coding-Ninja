# Problem statement
# Given an array ‘ARR’ and an integer ‘K’, your task is to find all the count of all sub-arrays whose sum is divisible by the given integer ‘K’.

# Note:
# If there exists no subarray in the given sequence whose sum is divisible by ‘K’ then simply return ‘0’.

def divisible_subarray_k(array:list[int],k:int)->int:
    
    n=len(array)
    count =0
    
    for start in range(n):
        
        curr =0
        
        for end in range(start,n):
            
            curr += array[end]
            
            if curr % k == 0:
                
                count +=1
                
    return count

arr = [2, 3, 4, 6]
k = 3
print(divisible_subarray_k(arr,k))