

#longest palindromic substring

def chek(string):
    
    return string==string[::-1]

def main(string):
    
    n=len(string)
    max_len=float("-inf")
    new=""

    for i in range(n):
        
        for j in range(i,n):
            
            substring=string[i:j+1]
            
            if chek(substring):
                
                length=j-i+1
                
                if length > max_len:
                    
                    max_len=length
                    new=substring
                    
    return new

a="badam"
print(main(a))