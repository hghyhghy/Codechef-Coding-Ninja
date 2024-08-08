# The function def differenceofSum(n. m) accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n.

# Assumption:

# n>0 and m>0
# Sum lies between integral range
# Example

# Input
# n:4
# m:20
# Output
# 90

def differenceofsum(n,m):
    
    divisible=0
    non_divisible=0
    
    for num in range(1,m+1):
        
        if num % n != 0 :
            
            non_divisible += num
            
        elif num % n == 0:
            
            divisible += num
            
            
    return non_divisible - divisible

n=4
m=20

print(differenceofsum(n,m))