#gcdlcf

def gdc(a,b):
    
    while b !=0:
        
        a,b=b,a%b
        
    return a

def lcm(a,b):
    
    return (a*b)//gdc(a,b)

a,b=list(map(int,input().split()))

gcd_value = gdc(a, b)
print(f"GCD of {a} and {b} is: {gcd_value}")

# Calculate LCM
lcm_value = lcm(a, b)
print(f"LCM of {a} and {b} is: {lcm_value}")