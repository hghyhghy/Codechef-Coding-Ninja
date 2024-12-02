# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

from collections import Counter

def common_character_between_two_word(s1,s2):
    
    Counter1 = Counter(s1)

    Counter2 = Counter(s2)

    common={}

    for char in Counter1:
        
        if char  in Counter2:
            
            common[char] = min(Counter1[char],Counter2,[char])

    
    result=[]

    for val,freq in common.items():
        
        result.extend([val] * freq)

    return result

word1 = "bella"
word2 = "label"

print(common_character_between_two_word(word1,word2))
    