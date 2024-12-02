# Problem statement
# You are having a string ‘S’ containing ASCII characters.



# You are required to reverse the input string.



# Output the reverse of the string ‘S’.

def reverse_string_using_pointers(string):
    
    string=list(string)
    
    n=len(string)
    left=0
    right=n-1
    
    while left < right:
        
        string[left],string[right] = string[right],string[left]
        left += 1
        right -= 1
        
    
    return "".join(string)

S = "hello"
print(reverse_string_using_pointers(S))