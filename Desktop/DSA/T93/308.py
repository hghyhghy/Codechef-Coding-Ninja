

#shortest subarray with minimum length

def main(array,k):
    
    n=len(array)
    minimum=float("inf")

    for i in range(n):
        
        current = 0
        
        for j in range(i,n):
            
            current += array[j]

            if current >=k:
                
                minimum=min(minimum,j-i+1)

                break
            
    return minimum

nums = [1, 2, 3, 4, 5]
k = 11

print(main(nums,k))