# Find all circular primes less than given number n. A prime number is a Circular Prime Number if all of its possible rotations are itself prime numbers.

import math

def is_prime(num):
    
    if num<=1:
        
        return False
    
    if num == 2 or num == 3:
        
        return True
    
    if num % 2 ==0 or num%3 ==0:
        
        return False
    
    limit=int(math.sqrt(num))
    for i in range(5,limit+1):
        
        if num % i == 0:
            
            return False
        
    return True

def generate_rotations(num):

    num_str=str(num)
    length=len(num_str)

    rotations=[]

    for i in range(length):
        
        rotation=num_str[i:]+ num_str[:i]
        rotations.append(int(rotation))

    return rotations

def checking_prime(n):

    store=[]

    for i in range(2,n):
        
        if is_prime(i):
            
            rotation=generate_rotations(i)

            if all(is_prime(i)for i in rotation):
                
                store.append(i)

    return store

n = int(input("Enter a number: "))
result = checking_prime(n)
print("Circular primes less than", n, ":", result)
                
    
    
    
    