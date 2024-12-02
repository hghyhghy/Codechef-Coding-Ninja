# Ninja and his friend are playing a game of subarrays. They have an array ‘NUMS’ of length ‘N’. Ninja’s friend gives him an arbitrary integer ‘K’ and asks him to find the length of the longest subarray in which the sum of elements is equal to ‘K’.

# Ninjas asks for your help to win this game. Find the length of the longest subarray in which the sum of elements is equal to ‘K’.

# If there is no subarray whose sum is ‘K’ then you should return 0.

# Example:
# Input: ‘N’ = 5,  ‘K’ = 4, ‘NUMS’ = [ 1, 2, 1, 0, 1 ]

# Output: 4

def longest_subarray_with_sum_k(arr,k):
    
    n=len(arr)
    max_lenght = 0 
    
    for start in range(n):
        
        current_sum = 0
        
        for end in range(start,n):
            
            current_sum += arr[end]

            if current_sum == k:
                
                lenght =  end-start + 1
                
                if lenght > max_lenght:
                    
                    max_lenght =  lenght
                    
    return max_lenght

arr = [1, 2, 3, 4, 5, -2, -3, 6]
K = 7

print(longest_subarray_with_sum_k(arr,K))