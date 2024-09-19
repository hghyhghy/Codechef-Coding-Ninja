# Problem statement
# You are given a string ‘str’ of even length. Your task is to find out if we divide the ‘str’ from the middle, will both the substrings contain an equal number of vowels or not.

# For Example:
# You are given, ‘str’= ‘codingninjas’, when we split this string we get, ‘coding’ and ‘ninjas’ which both contain 2 vowels each. Hence the answer is ‘True’.

def split_string(string):
    
    vowels=set('aeiouAEIOU')

    n=len(string)
    mid=n//2

    first_half=string[:mid]
    second_half=string[mid:]

    count1=sum(1 for char in first_half if char in vowels)
    count2=sum(1 for char in second_half if char in vowels)

    return count1==count2

str1 = "abcdxyEF"

print(split_string(str1))