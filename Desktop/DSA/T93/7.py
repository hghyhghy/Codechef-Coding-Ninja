#smallest substring  with all k character 

def main(s,x):
    
    seen=set(x)
    smallst=""
    
    n=len(s)
    
    for i in range(n):
        
        for j in range(i+1,n+1):
            
            substring=s[i:j]

            if seen.issubset(set(substring)):
                
                if not smallst or len(substring)<len(smallst):
                    
                    smallst =  substring
                    
    return smallst if smallst else  " "

s = "abdd"
x = "bd"
print(main(s,x))
        
        