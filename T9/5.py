# Reverse Every Word in A String

def reverse_word_in_string(s):
    
    def reverse_word(word):
        
        return word[::-1]
    
    words=s.split(' ')
    
    reverse_word=[reverse_word(word) for word in words]

    reversed_string= "".join(reverse_word)

    return reversed_string

s = "hello world"
print(reverse_word_in_string(s))