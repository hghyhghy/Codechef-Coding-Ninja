

#arrange alternative operations

def main(array):
    
    n=len(array)
    dp=[0]*n
    pos=0
    neg=1
    
    for num in array:
        
        if num >=0 :
            
            if pos<n:
                
                dp[pos] = num
                pos +=2
                
        else:
            
            if neg<n:
                
                dp[neg] = num
                neg +=2
                
    return dp
arr = [-1,1,2,-3,-4,6,5,-7]
print(main(arr))
                
                