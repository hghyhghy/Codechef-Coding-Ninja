# Problem statement
# Reverse the given string word wise. That is, the last word in given string should come at 1st place, last second word at 2nd place and so on. Individual words should remain as it is.

def reverse_string_word_wise(string:str)->str:
    
    word=string.split()
    
    reverse_word= word[::-1]
    
    return " ".join(reverse_word)

input_string = "Hello world this is Python"
print(reverse_string_word_wise(input_string))