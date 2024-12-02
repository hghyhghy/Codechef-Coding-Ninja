# Write a program to count and print the total number of characters (lowercase english alphabets only), digits (0 to 9) and white spaces (single space, tab i.e. '\t' and newline i.e. '\n') entered till '$'.

# That is, input will be a stream of characters and you need to consider all the characters which are entered till '$'.

# Print count of characters, count of digits and count of white spaces respectively (separated by space).

def count_characters(string):
    
    lowercase=0
    digit=0
    whitespace=0
    
    for char in string:
        
        if char == "$":
            
            break
        
        if  'a'<=char<='z':
            
            lowercase += 1
            
        elif '0'<=char<='9':
            
            digit += 1
            
        elif char == " " or char =="\n" or char =="\t":
            
            whitespace += 1
            
    return lowercase,digit,whitespace

input_string = input("Enter a stream of characters ending with $: ")
print(count_characters(input_string))
            
            