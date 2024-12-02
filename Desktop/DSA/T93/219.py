

#largest subarray sum

def main(array):
    
    n=len(array)
    max_len=float("-inf")

    for i in range(n):
        
        current = 0
        
        for j in range(i,n):
            
            current += array[j]

            max_len= max(max_len,current)

    
    return max_len

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(main(arr))