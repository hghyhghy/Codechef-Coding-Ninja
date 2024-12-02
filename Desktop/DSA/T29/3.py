#  Product Of Array Except Self

def product_of_array_except_itself(arry):
    
    n=len(arry)

    result=[1]*n
    
    for i in range(n):
        
        product= 1
        
        for j in range(n):
            
            if i != j:
                
                product *= arry[j]

        result[i] = product
        
    
    return result

arr = [1, 2, 3, 4]
print(product_of_array_except_itself(arr))