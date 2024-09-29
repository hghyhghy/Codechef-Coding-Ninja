# You are given a number 'N' in the form of a string 'S', your task is to find the smallest number strictly greater than the given number 'N' which is a palindrome.

# Note:

# 1) A palindrome is a word, number, phrase, or another sequence of characters that reads the same backward as forward, such as 'naman', 'abcba', '1234321', etc
# 2) The numerical value of the given string 'S' will be greater than 0.
# 3) A single-digit number is also considered as a palindrome.
# 4) Note that the length of the string 'S' is nothing but the number of digits in the number 'N'.

def is_palindrome(number):
    
    return number ==  number[::-1]

def checking_next_smaleest_palindrome(number):
    
    str_num= int(number)

    while True:
        
        str_num-= 1
        
        num = str(str_num)

        if is_palindrome(num):
            
            return num
    
a=1331
print(checking_next_smaleest_palindrome(a))


        
        