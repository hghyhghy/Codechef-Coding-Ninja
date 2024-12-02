

#smallest subarry with disctinc elemnts 

def main(array):
    
    n=len(array)
    max_len=0
    
    for i in range(n):
        
        seen=set()

        for j in range(i,n):
            
            seen.add(array[j])

            if len(seen) == j-i+1:
                
                max_len=min(max_len,j-i+1)

    return max_len

arr = [1, 2, 3, 2, 4, 5, 3]
print(main(arr))