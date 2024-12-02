

#count divisible pairs 

def main(n,m):
    
    count = 0
    
    for  i  in range(1,n+1):
        
        for j in range(1,m+1):
            
            if (i+j) % 5 == 0:
                
                count += 1
                
    return count

N = 5
M = 7

print(main(N,M))