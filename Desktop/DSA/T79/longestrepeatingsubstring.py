# You are given a string 'str' of length 'N'. You can perform at most 'k' operations on this string. In one operation, you can choose any character of the string and change it to any other uppercase English alphabet character.



# Return the length of the longest substring containing same characters after performing the above operations.



# For example :

# Input:
# str="AABC"  k=1

# Output:3

# Explanation: Replace 'B' with 'A', we will get "AAAC" and the longest substring with same character is "AAA" of length 3.

def longest_repeating_substring(string:str,k:int)->int:
    
    n=len(string)
    max_len= 0
    
    for i in range(n):
        
        for j in range(i,n):
            
            substring= string[i:j+1]
            
            freq = {}
            
            for char in substring:
                
                if char in freq:
                    
                    freq[char] +=1
                    
                else:
                    
                    freq[char] = 1
                    
                
            max_freq=  max(freq.values())
            
            length =j - i +1
            
            changes =  length - max_freq
            
            if changes <= k:
                
                max_len = max(max_len,length)
                
                
    return max_len

s = "AABABBA"
k = 1
print(longest_repeating_substring(s,k))