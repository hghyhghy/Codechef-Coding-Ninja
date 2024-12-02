

#maximum subarray sum 

def main(array):
    
    n=len(array)
    max_length = float("-inf")

    for i in range(n):
        
        curr = 0
        
        for j in range(i,n):
            
            curr += array[j]

            if curr>max_length:
                
                max_length = curr
                
                node=array[i:j+1]

    return max_length,node

arr = [1, 2, 7, -4, 3, 2, -10, 9, 1]
print(main(arr))