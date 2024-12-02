

#distinct

def main(array,k):
    
    n=len(array)
    r=[]

    for i in range(n-k+1):
        
        seen=set()
        for j in range(i,i+k):
            
            seen.add(array[j])

        
        r.append(len(seen))

    
    return r

arr = [1, 2, 2, 1, 3, 1, 1, 3]
k = 4

print(main(arr,k))