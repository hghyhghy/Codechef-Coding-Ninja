# You have been given a string STR. Your task is to find the total number of palindromic substrings of STR.

# Example :
# If the input string is "abbc", then all the possible palindromic substrings would be: ["a", "b", "b", c", "bb"] and hence, the output will be 5 since we have 5 substrings in total which form a palindrome.

def is_palindrome(string):
    
    return string == string[::-1]

def main(string):
    
    n=len(string)
    count = 0
    
    for start in range(n):
        
        for end in range(start,n):
            
            substring = string[start:end+1]
            
            if is_palindrome(substring):
                
                count += 1
                
    return count
s = "abbc"
print(main(s))
