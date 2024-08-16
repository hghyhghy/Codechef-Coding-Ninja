# Write a function that reverses a string. The input string is given as an array of characters s.

def reverse_string(string):
    
    left=0
    right=len(string) - 1
    
    while left <= right:
        
        string[left],string[right] = string[right],string[left]

        left += 1
        right -= 1
        
    
    return string

s = ['h', 'e', 'l', 'l', 'o']
print(reverse_string(s))