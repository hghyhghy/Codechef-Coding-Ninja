

def main(array):
    
    n=len(array)
    max_len=float("-inf")

    for i in range(n):
        
        current=0
        
        for j in range(i,n):
            
            current += array[j]

            if current == 0:
                
                length=j-i+1
                
                max_len=max(max_len,length)

    return max_len

arr = [1, 2, -2, 4, -4]
print(main(arr))

        