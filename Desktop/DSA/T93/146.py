

#count frequency 

def main(string):
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] +=1 
            
        else:
            
            freq[char] = 1
            
    return freq

a="abcdgd"
print(main(a))