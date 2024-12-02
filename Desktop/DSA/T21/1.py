# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

def addition_of_numbers(number):
    
    while number >= 10:
        
        number= sum(int(nums) for nums in str(number))
    
    return number

num = 38
print(addition_of_numbers(num))
    
    
    
    