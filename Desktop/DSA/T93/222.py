


#reverse string word wise 

def main(string:list[str])->list[str]:

    word=string.split()

    reversed_word =word[::-1]

    modified= " ".join(reversed_word)

    return modified

input_string = "Hello world this is OpenAI"
print(main(input_string))


    