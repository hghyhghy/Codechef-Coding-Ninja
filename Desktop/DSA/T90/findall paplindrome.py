# You are given an integer ‘N’. Your task is to find all palindromic numbers from 1 to ‘N’.

# Palindromic integers are those integers that read the same backward or forwards.

# Note:
# Order of numbers should be in the non-decreasing matter.
# For example:
# You are given ‘N’ as 12, so the output should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 11], as all single-digit numbers are palindromic, and 11 is also a palindromic number.

def check(num:int)->bool:
    
    return str(num).lower() == str(num)[::-1].lower()


def main_function(n:int)->list[int]:
    
    palindrome=[]

    for i in range(1,n+1):
        
        if check(i):
            
            palindrome.append(i)

    
    return palindrome if palindrome else -1

N = 12
print(main_function(N))