# Problem statement
# You have been given a number 'N'. Your task is to find the sum of all even numbers from 1 to 'N' (both inclusive).

# Example :

# Given 'N' : 6
# Sum of all even numbers till 'N' will be : 2 + 4 + 6 = 12

def sum_of_even_number_upto_n(limit):
    
    total = 0
    
    for num in range(1,limit+1):
        
        if num % 2 == 0:
            
            total += num
            
            
       
        
    return total

n=6
print(sum_of_even_number_upto_n(n))