

#reverse the string wordise

def main(string:str)->str:
    
    words=string.split()
    start=0
    end=len(words)-1
    
    while start < end:
        
        temp=words[start]
        words[start]=words[end]
        words[end] = temp
        
        start += 1
        end -= 1
        
    new="".join(words)

    return new

input_string = "Hello world from OpenAI"
print(main(input_string))