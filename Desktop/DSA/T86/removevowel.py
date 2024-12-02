# You are given a string STR of length N. Your task is to remove all the vowels present in that string and print the modified string.

# English alphabets ‘a’, ‘e’, ‘i’, ‘o’, ‘u’ are termed as vowels. All other alphabets are called consonants.

# Note: You have to only remove vowels from the string. There will be no change in the relative position of all other alphabets.

# For example:
# (i)  If the input string is 'CodeGeek', the output should be CdGk after removing ‘o’ and ‘e’.

# (ii) If the input string is 'Odinson', the output should be 'dnsn' after removing ‘o’ and ‘i’. 

def remove_vowels(string:str)->str:
    
    vowels="aeiouAEIOU"
    
    result=[]
    for char in string:
        
        if char in vowels:
            
            continue
        
        result.append(char)

    return "".join(result)

STR1 = 'CodeGeek'
print(remove_vowels(STR1))