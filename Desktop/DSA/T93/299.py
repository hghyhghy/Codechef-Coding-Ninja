

#maximum product 

def main(array):
    
    n=len(array)
    
    maximum=float("-inf")

    for i in range(n):
        
        for j in range(i+1,n):
            
            
            product = array[i] *array[j]

            maximum=max(maximum,product)

    
    return maximum

nums = [3,4,5,2]
print(main(nums))