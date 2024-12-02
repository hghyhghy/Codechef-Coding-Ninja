# Problem statement
# You are a string ‘S’. Your task is to count all the “substrings” of ‘S’ that contain only “vowels”.

# Note :
# 1. The string ‘S’ consists of only lowercase English alphabets.
# 2. A ‘substring’ is a contiguous sequence of characters within a string.
# 3. Recall that vowels in lowercase English alphabets are: {‘a’, ‘e’, ‘i’, ‘o’, ‘u’}.

def count_vowel_substring(string:str)->int:
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n=len(string)
    count  = 0

    for start in range(n):
        
        for end in range(start,n):
            
            if string[end] in vowels:
                
                count += 1
                
            else:
                
                break
            
    return count

s = "aeioubc"
print(count_vowel_substring(s))