

#minimum subarray with k distance 

def main(array,k):
    
    n=len(array)
    minimum=float("inf")

    for i in range(n-k+1):
        
        current= 0 
        
        for j in range(i,i+k):
            
            current += array[j]

        minimum = min(minimum,current)

    
    return current

arr = [2, 1, 5, 1, 3, 2]
k = 3

print(main(arr,k))