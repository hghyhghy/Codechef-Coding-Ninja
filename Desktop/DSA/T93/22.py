#next greater element

def main(array:list[int])->list[int]:
    
    n=len(array)
    dp=[-1]*n
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j]>array[i]:
                
                dp[i]=array[j]
                break
            
    return dp

arr = [1, 3, 2]
print(main(arr))