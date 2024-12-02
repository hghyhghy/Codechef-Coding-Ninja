# For a given input string(str), write a function to print all the possible substrings.

# Substring
# A substring is a contiguous sequence of characters within a string. 
# Example: "cod" is a substring of "coding". Whereas, "cdng" is not as the characters taken are not contiguous

def print_all_substring(string:str)->str:
    
    n=len(string)

    for i in range(n):
        
        for j in range(i+1,n+1):
            
            print(string[i:j])


input_string = "abc"
print(print_all_substring(input_string))