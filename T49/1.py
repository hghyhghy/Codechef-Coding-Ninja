# Problem statement
# You are given a string 'STR'. The string contains [a-z] [A-Z] [0-9] [special characters]. You have to find the reverse of the string.

# For example:

#  If the given string is: STR = "abcde". You have to print the string "edcba".
# follow up:
# Try to solve the problem in O(1) space complexity. 

def main_reverse(string):
    
    n=len(string)
    string=list(string)
    if not string or n==1:
        
        return None
    
    left=0
    right=n-1
    
    while left < right:
        
        string[left],string[right] = string[right],string[left]

        left += 1
        right -= 1
        
    return "".join(string)

a="coding"
print(main_reverse(a))


        
        