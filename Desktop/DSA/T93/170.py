

#next greater element 

def  main(array):
    
    n=len(array)
    dp=[-1]*n
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j] > array[i]:
                
                dp[i] =  array[j]

                break
            
    return dp

nums=list(map(int,input().split()))
print(main(nums))