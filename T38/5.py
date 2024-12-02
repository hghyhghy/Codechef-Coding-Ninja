# Problem statement
# For a given input string(str), write a function to print all the possible substrings.

# Substring
# A substring is a contiguous sequence of characters within a string. 
# Example: "cod" is a substring of "coding". Whereas "cdng" is not as the characters taken are not contiguous

def print_all_substrings(strings):
    
    n=len(strings)

    for i in range(n):
        
        
        for j in range(i+1,n+1):
            
            print (strings[i:j])


s="abc"
print(print_all_substrings(s))

        