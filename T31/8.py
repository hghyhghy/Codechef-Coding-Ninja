# Problem statement
# You are given two strings, 'str1' and 'str2'. You have to find the length of the longest common substring.



# A substring is a continuous segment of a string. For example, "bcd" is a substring of "abcd", while "acd" or "cda" are not.



# Example:
# Input: ‘str1’ = “abcjklp” , ‘str2’ = “acjkp”.

def longest_common_sequence(a1,a2):
    
    n=len(a1)
    m=len(a2)

    lenght = 0
    character=""

    for i in range(n):
        
        for j in range(1,n-i+1):
            
            substr=a1[i:i+j]

            if substr in a2:
                
                if j > lenght:
                    
                    lenght =j
                    character=substr
                    
    return character,lenght

s1 = "abcdef"
s2 = "zabcpqr"

print(longest_common_sequence(s1,s2))