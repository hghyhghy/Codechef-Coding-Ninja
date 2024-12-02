# Problem statement
# Given a number N, print sum of all even numbers from 1 to N.

def sum_upto_n(N):
    
    total=0
    for num in range(1,N+1):
        
        if num %2 == 0:
            
            total+=num
        
    return total

print(sum_upto_n(6))