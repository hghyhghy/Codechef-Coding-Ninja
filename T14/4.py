# calculate the sum of digits of a number 

def sum_of_digit_of_numbers(numbers):
    
    return sum(int(digit) for digit in str(numbers))

n="1234"
print(sum_of_digit_of_numbers(n))