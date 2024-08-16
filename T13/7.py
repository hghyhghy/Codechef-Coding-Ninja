# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

def non_space_segment(string):
    
    count = 0
    is_segment=False
    
    for char in string:
        
        if  char != " ":
            
            if not is_segment:
                
                count += 1
                is_segment = True
                
        else:
            
            if is_segment:
                
                is_segment=False
    
    return count

s = "Hello   world! This is  a test."
print(non_space_segment(s))