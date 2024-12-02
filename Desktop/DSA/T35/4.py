# Problem statement
# You are given a positive integer N, and you have to find the number of ways to represent N as a sum of cubes of two integers(let’s say A and B), such that:

# N = A^3 + B^3.

import math

def count_cubes(N):
    
    count=0
    limit=int(N**(1/3))+1
    
    for A in range(limit):
        
        B=N-A**3
        if B >=0:
            
            B_cubed= round(B**(1/3))

            if B_cubed **3 == B:
                
                count += 1
                
    return count

N = 1729
print(count_cubes(N))