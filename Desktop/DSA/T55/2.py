# Given a string S. For each index i(1<=i<=N-1), erase it if s[i] is equal to s[i-1] in the string.

def remove_consecutive_character(string):
    
    n=len(string)
    new_string=string[0]

    
    for i in range(1,n):
        
        if string[i] != string[i-1]:
            
            new_string += string[i]

    return new_string

S = "aabb"
print(remove_consecutive_character(S))