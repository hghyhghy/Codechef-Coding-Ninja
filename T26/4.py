# Reverse words in a string without using reverse/operator

def reverse_word_fo_the_string(string):
    
    words=string.split()

    start=0
    end=len(words)-1 
    
    while start < end:
        
        temp=words[start]
        words[start]=words[end]
        words[end]=temp
        
        start += 1
        end -= 1
        
    
    reverse_Word = "".join(words)

    return reverse_Word

input_string = "Hello world from OpenAI"
print(reverse_word_fo_the_string(input_string))