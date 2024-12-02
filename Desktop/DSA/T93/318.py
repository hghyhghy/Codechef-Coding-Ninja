

def main(string):
    
    def check(string):
        
        return len(string)==len(set(string))
    
    n=len(string)
    maximum=float("-inf")
    longest=""

    for i in range(n):
        
        for j in range(i+1,n+1):
            
            substring=string[i:j]

            if check(substring):
                
                if len(substring) > maximum:
                    
                    maximum=len(substring)
                    longest=substring
                    
    return longest

s = "abcabcbb"
print(main(s))
    
    