
#remove consecutive duplicate 

def main(string):
    
    n=len(string)
    new_string = string[0]

    for i in range(1,n):
        
        if string[i] != string[i-1]:
            
            new_string += string[i]
    
    return new_string

n=input("Enter s string")
print(main(n))
