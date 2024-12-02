# You are given an array 'A' of length 'N' consisting only of integers. You are also given three integers 'X', 'Y' and 'SUM'. Count the number of pairs ('i', 'j') where 'i' < 'j' such that ('A[i]' * 'X' + 'A[j]' * 'Y') = 'SUM'.

def count_pairs(array,x,y,target):
    
    n=len(array)
    count =0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if (array[i]*x +array[j]*y) == target:
                
                count += 1
                
    return count

A = [1, 2, 3, 4, 5]
X = 2
Y = 3
SUM1 = 11

print(count_pairs(A,X,Y,SUM1))