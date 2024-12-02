# Problem statement
# You are given a number ‘N’ and a query ‘Q.’ If ‘Q’ is 1, then you have to return the sum of all integers from 1 to ‘N,’ else if ‘Q’ is equal to 2 then you have to return the product of all integers from 1 to ‘N.’ Since the product can be very large, return it modulo 10 ^ 9 + 7.

def sum_or_product(n,q):
    
    mod=10**9 + 7
    
    if q == 1:
        
        return n*(n+1)//2
    
    elif q == 2:
        
        product=  1
        for i in range(1,n+1):
            
            product  *=  (product*i) % mod
            
        return product
    
N1, Q1 = 5, 1
print(sum_or_product(N1,Q1))