# You are given an integer ‘N’. Your task is to find all palindromic numbers from 1 to ‘N’.

# Palindromic integers are those integers that read the same backward or forwards.

# Note:
# Order of numbers should be in the non-decreasing matter.
# For example:
# You are given ‘N’ as 12, so the output should be [1, 2, 3, 4, 5, 6, 7, 8, 9, 11], as all single-digit numbers are palindromic, and 11 is also a palindromic number.

def is_palin(array):
    
    return array == array[::-1]

def check_palindrome(array):
    
    n=len(array)
    result=[]

    for start in range(n):
        
        for end in range(start,n):
            
            subarray=array[start:end+1]

            if is_palin(subarray):
                
                result.append(subarray)

    return result

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(check_palindrome(a))