# Problem statement
# You are given a string 'STR'. The string contains [a-z] [A-Z] [0-9] [special characters]. You have to find the reverse of the string.

# For example:

#  If the given string is: STR = "abcde". You have to print the string "edcba".
# follow up:
# Try to solve the problem in O(1) space complexity. 

def reverse_string_by_using_pointers(string):
    
    string=list(string)
    n=len(string)
    left=0
    right=n-1
    
    while left < right:
        
        string[left],string[right] = string[right],string[left]

        left += 1
        right -= 1
        
        
    return "".join(string)

input_string = "hello"

print(reverse_string_by_using_pointers(input_string))