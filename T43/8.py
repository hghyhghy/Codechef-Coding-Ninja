# Problem statement
# You are given two integers ‘N’ and ‘M’. A pair (x, y) is a divisible pair if it satisfies the following conditions:

# a) 1 <= x <= ‘N’

# b) 1 <= y <= ‘M’

# c) x + y is divisible by 5.

# Your task is to return the count of all divisible pairs that can be formed from given ‘N’ and ‘M’.


def checking_divisability(n,m):
    
    count = 0
    for  x in range(1,n+1):
        
        for y in range(1,m+1):
            if (x+y)%5 == 0:
                
                count += 1
                
    return count

N = 5
M = 5
print(checking_divisability(N,M))