

#longest palindrome

def main(string:str):

    new=string.split()

    reversed_word= new[::-1]

    return  "".join(reversed_word)

input_string = "Hello world this is Python"
print(main(input_string))

