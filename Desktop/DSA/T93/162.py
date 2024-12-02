


#main reverse 

def main(string):
    
    n=len(string)
    string=list(string)

    left=0
    right=n-1
    
    while left < right:
        
        string[left],string[right] =  string[right],string[left]

        left +=1 
        right -=1
        
    
    return "".join(string)

a="coding"
print(main(a))
