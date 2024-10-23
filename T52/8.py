# Given two variables ‘X’ and ‘Y’. Your task is to swap the number without using a temporary variable or third variable.

# Swap means the value of ‘X’ and ‘Y’ must be interchanged. Take an example ‘X’ is 10 and ‘Y’ is 20 so your function must return ‘X’ as a 20 and ‘Y’ as a 10.

def swap_two_numbers(x,y):
    
    if not x or not y:
        
        return
    
    x,y=y,x
    
    return x,y

x=10
y=12

print(swap_two_numbers(x,y))