

#find leaders 

def main(array):
    
    r=[]
    n=len(array)

    
    for i in range(n):
        
        flag=True
        
        for j in range(i+1,n):
            
            if array[i] <=array[j]:
                
                flag=False
                break
            
        if flag:
            
            r.append(array[i])

    return r

sequence = [16, 17, 4, 3, 5, 2]
print(main(sequence))