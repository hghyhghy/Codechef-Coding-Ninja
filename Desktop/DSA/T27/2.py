# Ninja has been given a binary string ‘STR’ containing either ‘0’ or ‘1’. A binary string is called beautiful if it contains alternating 0s and 1s.

# For Example:‘0101’, ‘1010’, ‘101’, ‘010’ are beautiful strings.

def is_beautiful_string(string):
    
    n=len(string) - 1
    
    for i in range(n):
        
        if string[i] == string[i-1]:
            
            return False
        
    return True


binary_string = "0101"
print(is_beautiful_string(binary_string))