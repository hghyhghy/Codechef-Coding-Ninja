# Int DigitSumDifference(int m, int n);

# Calculate and return the absolute difference between the sum of digits of numbers divisible by 4 and the sum of digits of numbers divisible by 7, in the range from ‘m’ to ‘n’ (inclusive).

# Note: 0 < m <= n

def difference_of_sum(m,n):
    
    temp=0
    temp1=0
    
    for i in range(m,n):
        
        if i % 4 ==0:
            
            temp += i
            
        elif i%7 ==0:
            
            temp1 += i
            
    return abs(temp-temp1)

m = 1  # Start of the range
n = 100

print(difference_of_sum(m,n))