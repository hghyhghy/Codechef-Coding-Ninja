# Replace all 0s with 1s in a given integer

def replace_by_one(array):
    
    
    num_str=str(array)

    replaced_char=""

    for char in num_str:
        
        if char == '0':
            
            replaced_char += '1'
            
        else:
            
            replaced_char +=char
            
    
    return int(replaced_char)


print(replace_by_one(102305))