# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

def  remove_duplicate_letter(string):
    
    result=list(( [char for char in string]))
    
    unique_index=1
    
    for i in range(1,len(result)):
        
        if result[i] != result[i-1]:
            
            result[unique_index] = result[i]

            unique_index += 1
    
    return unique_index

    

n="bcabc"
print(remove_duplicate_letter(n))