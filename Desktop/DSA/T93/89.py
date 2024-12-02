
#product of array except self

def main(array):
    
    n=len(array)

    dp=[-1]*n

    for i in range(n):
        
        product =1
        
        for j in range(n):
            
            if i!=j:
                
                product *= array[j]

        dp[i] =product
        
    
    return dp

arr=list(map(int,input().split()))
print(main(arr))