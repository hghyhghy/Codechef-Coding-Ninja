

#duplicate char in the string

def main(string):
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] +=1
            
        else:
            
            freq[char] =1
            
    
    for char,count in freq.items():
        
        if count > 1:
            
            return char,count
        
    return None

a="apple"
print(main(a))