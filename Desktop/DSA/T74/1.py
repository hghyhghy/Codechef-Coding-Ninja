# Ninja and his friend are playing a game of subarrays. They have an array ‘NUMS’ of length ‘N’. Ninja’s friend gives him an arbitrary integer ‘K’ and asks him to find the length of the longest subarray in which the sum of elements is equal to ‘K’.

# Ninjas asks for your help to win this game. Find the length of the longest subarray in which the sum of elements is equal to ‘K’.

# If there is no subarray whose sum is ‘K’ then you should return 0.

# Example:
# Input: ‘N’ = 5,  ‘K’ = 4, ‘NUMS’ = [ 1, 2, 1, 0, 1 ]

def longest_subarray_with_k_sum(array:list[int],k:int)->int:
    
    n=len(array)
    max_len=float("-inf")
    
    for start in range(n):
        
        curr = 0
        
        for end in range(start,n):
            
            curr += array[end]
            
            if curr == k:
                
                length = end-start +1
                
                max_len=max(max_len,length)
                
    return max_len

N = 5
K = 4
NUMS = [1, 2, 1, 0, 1]
print(longest_subarray_with_k_sum(NUMS,K))