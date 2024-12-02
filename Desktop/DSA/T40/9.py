# Problem statement
# You are given an integer 'n'. Calculate the sum of even and odd digits of 'n', represented in decimals.



# Even and odd do not refer to the position of the digit but to the polarity of the digit.



# Return the answer in the form of an array of size 2, such that the 0th index represents the even sum and the 1st index represents the odd sum.

def sum_of_even_odd_from_a_number(number):
    
    even=0
    odd=0
    
    for digit in str(number):
        
        digit=int(digit)

        if digit % 2 == 0:
            
            even += digit
            
        else:
            
            odd += digit
            
    return even,odd

n = 123456

print(sum_of_even_odd_from_a_number(n))