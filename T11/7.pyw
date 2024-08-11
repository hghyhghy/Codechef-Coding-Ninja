# Problem 1: Write a program to find the count of numbers that consists of unique digits.
# Input:

# Input consists of two Integer lower and upper values of a range

# Output:

# The output consists of a single line and prints the count of unique digits in a given range. Else Print"No Unique Number"

def count_of_unique_digits(m,n):
    
    def has_unique(num):
        
        num_str=str(num)

        return len(set(num_str))== len(num_str)

    
    count = 0
    for num in range(m,n+1):
        
        if has_unique(num):
            
            count += 1
            
    
    if count:
        
        return count
    
    else:
        
        return "No unique elements"

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

print(count_of_unique_digits(lower,upper))