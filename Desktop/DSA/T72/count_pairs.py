# Problem statement
# You are given two integers ‘N’ and ‘M’. A pair (x, y) is a divisible pair if it satisfies the following conditions:

# a) 1 <= x <= ‘N’

# b) 1 <= y <= ‘M’

# c) x + y is divisible by 5.

# Your task is to return the count of all divisible pairs that can be formed from given ‘N’ and ‘M’.

 

# Example :
# If N = 3 and M = 5, then { x = 1, y = 4 },  { x = 2, y = 3 },  { x = 3, y = 2 } are the pairs that satisfy the given conditions.

def count_divisible_pairs(n:int,m:int)->int:
    
    count =0
    
    for i in range(1,n+1):
        
        for j in range(1,m+1):
            
            if (i+j)%5 == 0:

                count +=1
                
    return count

print(count_divisible_pairs(4,6))