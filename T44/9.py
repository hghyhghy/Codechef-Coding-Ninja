# Problem statement
# You are given an integer ‘N’. Your task is to find all palindromic numbers from 1 to ‘N’.

# Palindromic integers are those integers that read the same backward or forwards.

# Note:
# Order of numbers should be in the non-decreasing matter.
# For example:
# You are given ‘N’ as 12, so the output should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 11], as all single-digit numbers are palindromic, and 11 is also a palindromic number.

def checking_palindrome(string):
    
    return string == string[::-1]

def main(arr):
    
    n=len(arr)
    max_lenght=0
    palindrome=[]

    for start in range(n):
        
        for end in range(start,n):
            
            substring = arr[start:end+1]
            if checking_palindrome(substring):
                
                
                lenght=len(substring)
                if lenght > max_lenght:
                    max_lenght =max(max_lenght,lenght)
                    palindrome=substring
                
    return palindrome

arr = [1, 2, 3, 2, 1, 4, 5, 4, 2, 1]
print(main(arr))