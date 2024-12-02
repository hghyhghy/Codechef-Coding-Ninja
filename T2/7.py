# # Given a string str, a character ch1, and a character ch2, replace all occurrences of ch1 in str with ch2 and vice versa.
# str = “apples”, ch1 = ‘a’, ch2 = ‘p’

 	 	
# str = “paales”

def character_replace(str,c1,c2):
    
    trasnformed_str=""

    for i in range (len( str)):
        
        if str[i] == c1:
            
            trasnformed_str += c2
            
        elif str[i] ==  c2:
            
            trasnformed_str += c1
            
            
        else :
            
            trasnformed_str += str[i]

    return trasnformed_str

str = "apples"
ch1 = "a"
ch2 = "p"

print(character_replace(str,ch1,ch2))