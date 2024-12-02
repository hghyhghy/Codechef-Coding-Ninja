# Problem statement
# You are given two strings, 'str1' and 'str2'. You have to find the length of the longest common substring.



# A substring is a continuous segment of a string. For example, "bcd" is a substring of "abcd", while "acd" or "cda" are not.



# Example:
# Input: ‘str1’ = “abcjklp” , ‘str2’ = “acjkp”.

# Output: 3

# Explanation:  The longest common substring between ‘str1’ and ‘str2’ is “cjk”, of length 3.

def longest_common_substring(string1:str,string2:str)->int:
    
    seen=set()
    longest = ""
    n1=len(string1)
    
    for i in range(n1):
        
        for j in range(i+1,n1+1):
            
            substring =  string1[i:j]
            seen.add(substring)
            
    n2=len(string2)
    
    for i in range(n2):
        
        for j in range(i+1,n2+1):
            
            substring1=  string2[i:j]
            
            if substring1 in seen and len(substring1)>len(longest):
                
                longest =  substring1
                
    return len(longest)

str1 = "abcdxyz"
str2 = "xyzabcd"
print(longest_common_substring(str1,str2))