

def main(string):
    
    n=len(string)
    longest=""
    max_length=0
    
    for i in range(n):
        
        seen=set()
        substring=""

        for j in range(i,n):
            
            
            if string[j] in seen:
                
                break
            
            seen.add(string[j])
            substring += string[j]
            length = j-i+1
            
            if length > max_length:
                
                max_length =  length
                longest =  substring
                
                
    return longest

s = "abcabcbb"
print(main(s))