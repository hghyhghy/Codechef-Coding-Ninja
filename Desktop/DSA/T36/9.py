# Problem statement
# Reverse the given string word-wise. The last word in the given string should come at 1st place, the last-second word at 2nd place, and so on. Individual words should remain as it is.

def reverse_string_word_wise(string):
    
    word=string.split()
    reversed_word=word[::-1]

    modified = " ".join(reversed_word)

    return modified

input_string = "Hello world this is OpenAI"
print(reverse_string_word_wise(input_string))

