


#product of the array except self

def main(array):
    
    n=len(array)
    dp=[1]*n
    
    for i in range(n):
        
        product = 1
        
        for j in range(i+1,n):
            
            if array[i] != array[j]:
                
                product *= array[j]

        
        dp[i] = product
        
    return dp

nums = [1,2,3,4]
print(main(nums))