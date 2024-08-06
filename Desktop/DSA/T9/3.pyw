# longest subarray with max product 

def max_subarray_product(array):
    
    n=len(array)
    max_prduct=float('-inf')

    for start in range(n):
        
        current_product = 1
        
        for end in range(start,n):
            
            current_product *= array[end]

            max_prduct = min(max_prduct,current_product)

    return max_prduct

array = [2, 3, -2, 4]
print(max_subarray_product(array))