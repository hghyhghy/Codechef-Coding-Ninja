
#maximum product subarray 

def main(array:list[int])->int:
    
    n=len(array)
    max_product=float("-inf")

    for i in range(n):
        
        product=1
        
        for j in range(i,n):
            
            product *= array[j]

            max_product = max(max_product,product)

    return max_product

arr=list(map(int,input().split()))
print(main(arr))