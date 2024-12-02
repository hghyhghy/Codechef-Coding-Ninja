


#longest palindrome

def check(string:str):

    return  string.lower() == string[::-1].lower()

def main(string):

    n=len(string)
    new=""
    maximum=float("-inf")

    for i in range(n):

        for j  in range(i,n):

            substring=string[i:j+1]

            if check(substring):

                if len(substring) > maximum:

                    maximum=len(substring)
                    new=substring


    return  new


s = "ababc"
print(main(s))