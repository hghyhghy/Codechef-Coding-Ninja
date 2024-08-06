# check whether two strings are anagram or not 

def anagrams(string1,string2):
    
    string1 = "".join(string1.split()).lower()
    string2 = "".join(string2.split()).lower()

    if len(string1) != len(string2):
        
        return False
    
    return sorted(string1) == sorted(string2)

print(anagrams("Listen", "Silent"))
