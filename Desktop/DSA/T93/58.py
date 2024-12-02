
#maximum product subarray 

def main(array):
    
    n=len(array)
    max_product =float("-inf")
    
    for i in  range(n):
        
        product =1 
        
        for j in range(i,n):
            
            product *= array[j]

            if product > max_product:
                
                max_product = product
                
    return max_product

arr=list(map(int,input().split()))
print(main(arr))