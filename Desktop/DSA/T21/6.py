# 383. Ransom Note
# Easy
# Topics
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

from collections import Counter

def is_constructed(ransomnote,magazine):
    
    ransom_count = Counter(ransomnote)

    magazine_count= Counter(magazine)

    for val,count in ransom_count.items():
        
        if magazine_count[val]< count:
            
            return False
        
    return True

ransomNote = "aabbcc"
magazine = "abcabcabc"
print(is_constructed(ransomNote,magazine))