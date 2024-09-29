# Problem statement
# Given an array arr of size N containing positive and negative integers. Arrange the array alternatively such that every non-negative integer is followed by a negative integer and vice-versa.

def alternative_rearrangement(array):
    
    n=len(array)
    dp=[0]*n
    posi=0
    neg=1
    
    for num in array:
        
        if  num >= 0:
            
            if posi <n:
                
                dp[posi] =  num
                posi += 2
                
        else:
            
            if neg < n:
                
                dp[neg] = num
                neg += 2
                
                
    return dp

arr = [1, -2, 3, -4, 5, -6, -7, 8]
print(alternative_rearrangement(arr))