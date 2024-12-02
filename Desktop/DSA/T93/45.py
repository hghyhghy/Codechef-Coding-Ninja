

#first unique character 

def main(array):
    
    freq={}
    for char in array:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
    
    for char in array:
        
        if freq[char] ==1:
            
            return char
    
    return -1

a=input("enter string")
result = main(a)
print(f"First unique character: {result}")