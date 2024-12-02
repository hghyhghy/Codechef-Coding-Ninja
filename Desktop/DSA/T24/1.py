# Maximum product subarray in an array

def maximum_product_subarray(arr):
    
    n=len(arr)
    max_product=0
    
    for start in range(n):
        
        current_product= 1
        
        for end in range(start,n):
            
            current_product *= arr[end]

            max_product = max(current_product,max_product)

    return max_product

nums = [2, 3, -2, 4]
print(maximum_product_subarray(nums))