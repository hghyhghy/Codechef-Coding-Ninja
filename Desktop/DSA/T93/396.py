
#checking palindrome

def check(string:str):

    return  string.lower() == string[::-1].lower()

def main(string):

    n=len(string)

    for i in range(n):

        newstring=string[:i]+string[i+1:]

        if check(newstring):

            return  True


    return  False

s = "abca"
print(main(s))