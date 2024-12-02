

#minimum subarray sum

def main(array):
    
    n=len(array)
    minimum=float("inf")

    for i in range(n):
        
        current =0 
        
        for j in range(i,n):
            
            current += array[j]

            minimum=min(minimum,current)
            
    return minimum

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(main(arr))