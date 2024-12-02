 
#subarray sum with equal no of one and zero

def main(array):
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n):
        
        one=0
        zero=0
        
        for j in range(i,n):
            
            if array[j] == 0:
                
                zero += 1
                
            if array[j] == 1:
                one += 1
                
            
            if one ==  zero:
                
                maximum = max(maximum,j-i+1)
                
    return maximum

arr=list(map(int,input().split()))
print(main(arr))