
#reverser string using pointers 

def main(string):
    
    n=len(string)
    left=0
    right=n-1
    
    string=list(string)

    while left < right:
        
        string[left],string[right]= string[right],string[left]

        left  +=1
        right -=1
        
    return "".join(string)

S = "hello"
print(main(S))