# reverse each word from the string 

def reverse_each_word_from_string(string):
    
    words=string.split()

    reverse_word=[word[::-1] for word in words]

    reverse_string= "".join(reverse_word)

    return reverse_string

s = "Hello World"
print(reverse_each_word_from_string(s))