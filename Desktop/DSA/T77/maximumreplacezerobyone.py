# Problem statement
# Given a binary array 'ARR' of size 'N', your task is to find the longest sequence of continuous 1’s that can be formed by replacing at-most 'K' zeroes by ones. Return the length of this longest sequence of continuous 1’s.

def maximum_remove_zero(array:list[int],k:int)->int:
    
    n=len(array)
    max_len=float("-inf")
    
    for  i in range(n):
        
        count = 0 
        
        for j in range(i,n):
            
            if array[j]==0:
                
                count +=1
                
            if count > k:
                
                break
            
            max_len =max(max_len,j-i+1)
            
    return max_len
