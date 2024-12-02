
# Code
# Testcase
# Test Result
# Test Result
# 395. Longest Substring with At Least K Repeating Characters
# Medium
# Topics
# Companies
# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

# if no such substring exists, return 0.

 

def longest_substirng_with_k_freq_elements(string,k):
    
    n=len(string)
    max_len= float("-inf")

    for  i in range(n):
        
        freq ={}

        for j in range(i,n):
            
            char =  string[j]

            if char in freq:
                
                freq[char] += 1
                
            else:
                
                freq[char] = 1
            
            if all(count >= k  for count in freq.values()):
                
                max_len = max(max_len,j-i+1)
                
    return max_len

s = "aaabb"
k = 3
print(longest_substirng_with_k_freq_elements(s,k))    
        