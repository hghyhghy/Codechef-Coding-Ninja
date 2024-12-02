# most number of palindrome

def check(string:str)->bool:
    
    return string == string[::-1]

def main(string:str)->int:
    
    n=len(string)
    count= 0
    
    for start in range(n):
        
        for end in range(start,n):
            
            substring = string[start:end+1]
            
            if  check(substring):
                
                count += 1
                
    return count

a="abc"
print(main(a))