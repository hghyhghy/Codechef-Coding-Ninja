# Problem statement
# Given an array arr of length N consisting of positive and negative integers, return the length of the longest subarray whose sum is zero.

def maximum_subarray(array:list[int])->int:
    
    n=len(array)
    max_len=float("-inf")
    
    for start in range(n):
        
        curr = 0
        
        for end in range(start,n):
            
            curr +=array[end]
            
            if curr == 0:
                
                length = end-start+1
                
                max_len = max(max_len,length)
                
    return max_len

arr = [1, 2, -3, 3, 1, -1, 2, -2]
print(maximum_subarray(arr))