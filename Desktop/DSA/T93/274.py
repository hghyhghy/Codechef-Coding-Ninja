

#removal of alphabets 

def main(array):
    
    numbers="123456789"
    new=""

    for char in array:
        
        if char in numbers:
            
            break
        
        else:
            
            new += char
            
    return new 

print(main("Hello, World! 123"))
