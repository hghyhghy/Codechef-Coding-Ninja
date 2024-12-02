# You are given two strings 'str1' and 'str1'.



# You have to tell whether these strings form an anagram pair or not.



# The strings form an anagram pair if the letters of one string can be rearranged to form another string.

# Pre-requisites:

# Anagrams are defined as words or names that can be formed by rearranging the letters of another word. Such as "spar" can be formed by rearranging letters of "rasp". Hence, "spar" and "rasp" are anagrams.

from collections import Counter

def check_anagram_pair(string1:str,string2:str) -> bool:
    
    if len(string1) != len(string2):
        
        return False
    
    string1 =string1.replace(" ","").lower()
    string2 = string2.replace(" ","").lower()

    return Counter(string1) ==  Counter(string2)

print(check_anagram_pair("listen", "silent"))
    
    