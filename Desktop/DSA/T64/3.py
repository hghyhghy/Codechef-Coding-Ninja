# You have been given a string STR. Your task is to find the total number of palindromic substrings of STR.

# Example :
# If the input string is "abbc", then all the possible palindromic substrings would be: ["a", "b", "b", c", "bb"] and hence, the output will be 5 since we have 5 substrings in total which form a palindrome.
# Note :
# A string is said to be a 'Palindrome' if it is read the same forwards and backwards. 
# For example, “abba” is a palindrome, but “abbc” is not.

# A 'Substring' is a contiguous sequence of characters within a string. 
# For example, "a", "b", "c", "ab", "bc", "abc" are substrings of "abc".

def check(string):
    
    return string==string[::-1]

def counting_palindrome(string):
    
    count=0
    n=len(string)

    for start in range(n):
        
        for end in range(start,n):
            
            substring=string[start:end+1]
            
            if check(substring):
                
                count += 1
                
    return count

a="abc"
print(counting_palindrome(a))