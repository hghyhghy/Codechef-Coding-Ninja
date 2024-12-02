# 30 upvotes
# Asked in companies
# Problem statement
# You are given string S of length N, and an integer K. Your task is to find the length of the longest substring that contains at most K distinct characters.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10
# 1 <= K <= 26
# 1 <= N <= 10^4

# Time Limit: 1sec

def longest_substring_with_k_distinct_elements(array:list[int],k:int)->int:
    
    n=len(array)
    max_len=float("-inf")
    
    for i in range(n):
        
        seen=set()
        
        for j in range(i,n):
            
        
            seen.add(array[j])
            
            if len(seen)>k:
                
                break
            max_len =max(max_len,j-i+1)
    
    return max_len

s = "eceba"
k = 2
print(longest_substring_with_k_distinct_elements(s,k))