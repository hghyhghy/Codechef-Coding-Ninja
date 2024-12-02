# You are given a string 'str' and an integer ‘K’. Your task is to find the length of the largest substring with at most ‘K’ distinct characters.

# For example:
# You are given ‘str’ = ‘abbbbbbc’ and ‘K’ = 2, then the substrings that can be formed are [‘abbbbbb’, ‘bbbbbbc’]. Hence the answer is 7.

def longest_substribng_with_k_diff_elements(array:list[int],k:int)->int:
    
    n=len(array)
    max_len=float("-inf")
    
    for i in range(n):
        
        seen=set()
        
        for j in range(i,n):
            
            seen.add(array[j])
            
            if len(seen) <= k:
                
                max_len =max(max_len,j-i+1)
                
            else:
                
                break
            
    return max_len

s = "abbbbbbc"
K = 2
print(longest_substribng_with_k_diff_elements(s,K))