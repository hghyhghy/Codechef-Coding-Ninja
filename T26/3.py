# Write a program to find a substring within a string. If found display its starting position

def find_substring(string,sub):
    
    position= string.find(sub)

    if position != -1:
        
        return position
    
    else:
        
        return -1
    
main_string = "Hello, welcome to the world of Python."
substring = "welcome"

print(find_substring(main_string,substring))
    
    
    