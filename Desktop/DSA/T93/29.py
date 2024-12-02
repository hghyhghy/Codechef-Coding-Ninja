#remove consecutive duplicate 

def main(string:str)->str:
    
    result=string[0]
    n=len(string)
    
    for i in range(1,n):
        
        if string[i] != string[i-1]:
            
            result += string[i]
    
    return "".join(result)


i=list(map(str,input("enter").split()))

for string in i:
    
    print(main(string))