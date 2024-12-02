# You are given two strings ‘S1’ and ‘S2’. Your task is to find the smallest substring of ‘S1’ which contains all the characters of ‘S2’. The characters of ‘S2’ need not be present in the same order in S1. That is, we need a substring that contains all characters of ‘S2’ irrespective of the order.

# A substring is a contiguous sequence of characters within a string.

# Example

# Let ‘S1’ be “ABBCD” and ‘S2’ be “ABC”, so the smallest substring of ‘S1’ which contains all the characters of S1 is “ABBA”.

from collections import Counter

def contains_all_char(s1,target):

    freq1=Counter(s1)

    for char in target:
        
        if freq1[char] < target[char]:
            
            return False
        
    
    return True

def smallest_substring(s1,s2):
    
    n=len(s1)
    result=""
    minimum=float("inf")

    target=Counter(s2)

    
    for i in range(n):
        
        for j in range(i+1,n+1):
            
            substring =  s1[i:j]

            if contains_all_char(substring,target):
                
                if len(substring)< minimum:
                    
                    minimum=  len(substring)
                    result=substring
                    
    
    return result if result else -1

S1 = "ABBCD"
S2 = "ABC"

print(smallest_substring(S1,S2))
    
    
    