# Problem statement
# You are given a string 'S'. Your task is to check whether the string is palindrome or not. For checking palindrome, consider alphabets and numbers only and ignore the symbols and whitespaces.

# Note :

# String 'S' is NOT case sensitive.
# Example :

# Let S = “c1 O$d@eeD o1c”.
# If we ignore the special characters, whitespaces and convert all uppercase letters to lowercase, we get S = “c1odeedo1c”, which is a palindrome. Hence, the given string is also a palindrome.

def is_palindrome(string:str)->bool:
    
    new=[char.lower() for char in string if char.isalnum()]
    
    new_str=" ".join(new)

    return new_str == new_str[::-1]

s = "c1 O$d@eeD o1c"
print(is_palindrome(s))