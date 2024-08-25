# Calculate frequency of characters in a string

def frequency_of_each_char(string):
    
    count={}

    
    for char in string:
        
        if char in count:
            
            count[char] += 1
            
        else:
            
            count[char] = 1
            
            
    return count

string = "hello world"
print(frequency_of_each_char(string))