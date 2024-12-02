# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

def reverse_words_of_string(string):
    
    words=string.split()

    reversed_word=words[::-1]

    reversed_string = " ".join(reversed_word)

    return reversed_string

s1 = "the sky is blue"
print(reverse_words_of_string(s1))

    
