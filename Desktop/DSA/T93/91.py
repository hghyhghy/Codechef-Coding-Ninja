
#most freq meeting 

def main(string):

    freq={}
    
    for char in string:
        
        if  char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1

    result={char:count for char,count in freq.items() if count > 1}
    
    return result

string=input("enter")
print(main(string))
    
    