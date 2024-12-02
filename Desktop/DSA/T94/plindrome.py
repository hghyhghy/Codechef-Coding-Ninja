#
# 3.	Write code to check a String is palindrome or not.
# Explanation: A string is called a palindrome if the reverse of the string is the same as the original one. For example, “madam”, “12321”.


def palindrome(string:str):

    n=len(string)
    string=string.replace(" ","").lower()

    left=0
    right=n-1

    while left < right:

        if string[left] != string[right]:

            return  False

        left +=1
        right -=1

    return True

s="madam"
print(palindrome(s))