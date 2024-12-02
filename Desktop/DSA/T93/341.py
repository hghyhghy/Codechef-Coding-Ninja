

#check palindrome

def func(string):

    string="".join(c.lower() for c in string if c.isalnum())

    left =0
    right=len(string)-1

    while left < right:

        if string[left] != string[right]:

            return  False

        left +=1
        right -=1


    return  True

print(func("A man, a plan, a canal, Panama"))
