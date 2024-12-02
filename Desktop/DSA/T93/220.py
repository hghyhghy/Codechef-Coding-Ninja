

#maximum product subarray 

def main(array):
    
    n=len(array)
    max_product=float("-inf")

    for i in range(n):
        
        product =1
        
        for j in range(i,n):
            
            product *= array[j]

            max_product=max(max_product,product)

    return max_product

arr = [2, 3, -2, 4]
print(main(arr))


    