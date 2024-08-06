	
# Largest odd number in a string

def largest_odd_number_from_string(string):
    
    number=[]
    store=""

    for char in string:
        
        if char.isdigit():
            
            store += char
            
        else:
            
            if store:
                
                number.append(int(store))
                store =""


    if store:
        
        number.append(int(store))

    odd_number=[num for num in number if num%2 != 0]

    if odd_number:
        
        return max(odd_number)
    
    else:
        
        return None
    
s = "The numbers are 123, 456, 789, and 101."
print(largest_odd_number_from_string(s))
    
            