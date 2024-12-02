

#contains duplicate at k distance

def main(array,k):
    
    n=len(array)
    seen=set()
    

    for i in range(n):
        
        
        for j in range(i,i+k):
            
            if array[j] in seen:
                
                return  True
            
            else:
            
                seen.add(array[j])

    return False


arr = [1, 2, 3, 1]
K = 3

print(main(arr,K))