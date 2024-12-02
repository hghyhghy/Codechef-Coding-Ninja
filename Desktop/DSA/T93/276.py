

#count 

def main(string):
    
    freq={}

    for char in  string:
        
        if char in freq:
            
            freq[char] +=1 
            
        else:
            
            freq[char] =1 
            
    
    return freq

string = "hello world"
print(main(string))