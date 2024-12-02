# Problem Statement: Given two strings, write a program to remove characters from the first string which are present in the second string.

def removing_character_from_common_strings(s1,s2):
    
    common_result=[]

    for char in s1:
        
        should_remove=False
        
        for char1 in s2:
            
            if char ==  char1:
                
                should_remove = True
                
                break
            
            
        if not should_remove:
            
            common_result.append(char)

    return "".join(common_result)       


s1 = "hello"
s2 = "oe"

print(removing_character_from_common_strings(s1,s2))