# You are given an array 'ARR' of 'N' integers and two integers 'K' and 'M'.

# You need to return true if the given array can be divided into pairs such that the sum of every pair gives remainder 'M' when divided by 'K'. Otherwise, you need to return false.

def valid_pairs(array,k,m):
    
    n=len(array)
    
    result=False
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            store=array[i] + array[j]
            
            if store % k == m:
                
                result=True
                
    return result

ARR = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
K = 5
M = 0

print(valid_pairs(ARR,K,M))