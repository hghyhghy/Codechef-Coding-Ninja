# Problem statement
# Ninja loves playing with numbers. So his friend gives him an array on his birthday. The array consists of positive and negative integers. Now Ninja is interested in finding the length of the longest subarray whose sum is zero.

def longest_subarray_with_zero_sum(array:list[int]):
    
    n=len(array)
    max_len=0
    
    for i in range(n):
        
        curr=0
        
        for j in range(i,n):
            
            curr += array[j]
            
            if curr == 0:
                
                max_len =max(max_len,j-i+1)
                
    return max_len

arr = [1, -1, 3, 2, -2, -3, 3]
print(longest_subarray_with_zero_sum(arr))