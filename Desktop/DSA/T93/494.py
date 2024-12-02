
#checking palindrome

def main(string:str):

    new = [char.lower() for char in string if char.isalnum()]

    new_char=" ".join(new)

    return new_char == new_char[::-1]

s = "c1 O$d@eeD o1c"
print(main(s))
