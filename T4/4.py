# Return maximum occurring character in the input string

def maximum_occuring_character(string):
    
    frequecny={}

    for char in string:
        
        if char in frequecny:
            
            frequecny[char] += 1
            
        else:
            
            frequecny[char] = 1
            
    store=[]
    max_char=-1
    
    for val,count in frequecny.items():
        
        if count > max_char:
            
            store=[val]
            max_char=count
            
        elif count == max_char:
            
            store.append(val)

            
    return store,frequecny

str = "takeuforward"
print(maximum_occuring_character(str))