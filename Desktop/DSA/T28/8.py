# Problem statement
# You are given a positive integer ‘n’.



# Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of sqrt(n).


import math

def sqrt_of_positive_integer(n):
    
    number=math.sqrt(n)

    return math.floor(number)

n = 27
print(sqrt_of_positive_integer(n))