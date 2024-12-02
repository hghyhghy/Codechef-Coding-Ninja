# You have been given a number 'N'. Your task is to find the sum of all even numbers from 1 to 'N' (both inclusive).

# Example :

# Given 'N' : 6
# Sum of all even numbers till 'N' will be : 2 + 4 + 6 = 12

def sum_even_odd(n:int)->int:
    
    num = 0
    
    for i in range(2,n+1,2):
        
        num += i
        
    return num
a=6
print(sum_even_odd(a))