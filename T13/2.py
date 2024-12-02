# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def reverse_vowels_from_string(string):
    
    vowels = set('aeiouAEIOU')

    stack=[char for char in string if char in vowels]

    result = []

    for char in string:
        
        if char in vowels:
            
            result.append(stack.pop())

        else:
            
            result.append(char)
            
    
    return "".join(result)


s="hello"
print(reverse_vowels_from_string(s))