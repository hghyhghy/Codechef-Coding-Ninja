# You have been given an integer array/list (ARR) of size N. You have to return an array/list PRODUCT such that PRODUCT[i] is equal to the product of all the elements of ARR except ARR[i]

def product_of_array_except_self(array):
    
    n=len(array)
    dp=[1]*n
    
    for i in range(n):
        
        product= 1
        
        for j in range(n):
            
            if i !=j:
                
                product *= array[j]
                
        dp[i] = product
    
    return dp

arr = [1, 2, 3, 4]
print(product_of_array_except_self(arr))