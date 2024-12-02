# Check if two strings are anagram of each other

def check_if_anargrams(s1,s2):
    
    str1=s1.replace(" ","").lower()
    
    str2=s2.replace(" ","").lower()

    return sorted(str1) ==  sorted(str2)

print(check_if_anargrams("Listen", "Silent"))