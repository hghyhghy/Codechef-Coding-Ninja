# Problem statement
# You are given a number 'N' in the form of a string 'S', your task is to find the smallest number strictly greater than the given number 'N' which is a palindrome.

# Note:

# 1) A palindrome is a word, number, phrase, or another sequence of characters that reads the same backward as forward, such as 'naman', 'abcba', '1234321', etc
# 2) The numerical value of the given string 'S' will be greater than 0.
# 3) A single-digit number is also considered as a palindrome.
# 4) Note that the length of the string 'S' is nothing but the number of digits in the number 'N'.

def is_palin(nums):
    
    return str(nums) == str(nums)[::-1]

def next_smallest_palin(nums):
    
    n=int(nums)

    n += 1
    
    while not is_palin(n):
        
        n += 1
        
    return str(n)

a="1221"
print(next_smallest_palin(a))
