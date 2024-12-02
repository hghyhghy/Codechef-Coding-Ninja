

#the maximum product of three numbers 

def main(array):
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                product = array[i] * array[j] * array[k]
                
                maximum=max(maximum,product) 

    return maximum

nums=list(map(int,input().split()))
print(main(nums))