
# nth fibonacci number 

def nth_fibonacci_number(n):

    if n<=0:

        return 0
    
    elif n == 1:

        return 1
    
    else:

        return nth_fibonacci_number(n-1) + nth_fibonacci_number(n-2)
    
n=10

print(nth_fibonacci_number(n))