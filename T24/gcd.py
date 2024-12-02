# GCD of two numbers

def gcd(a,b):
    
    while b:
        
        a,b= b, a%b
        
    return a

def lcm(a,b):
    
    return abs(a*b)//gcd(a,b)

print(gcd(48, 18))
print(lcm(12, 15))