# Problem statement
# Reverse the given string word-wise. The last word in the given string should come at 1st place, the last-second word at 2nd place, and so on. Individual words should remain as it is.

def reverse_senstence_word_wise(sentence:str)->str:
    
    word=sentence.split()

    reversed_word=[]
    n=len(word)

    for i in range(n-1,-1,-1):
        
        reversed_word.append(word[i])

    new=" ".join(reversed_word)

    return new 

input_string = "Hello world this is OpenAI"
print(reverse_senstence_word_wise(input_string))
    
