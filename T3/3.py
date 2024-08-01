# Int ReverseAndAdd(int m, int n);

# Calculate and return the sum of numbers obtained by reversing the digits of each number in the range from ‘m’ to ‘n’ (inclusive).

# Note: 0 < m <= n

def reverse_num(num):
    
    return int(str(num)[::-1])


def total_sum(n,m):
    
    total=0
    
    for i in range(m,n+1):
        
        nums = reverse_num(i)

        total += nums
    
    return total

m = 1  # Start of the range
n = 10

print(total_sum(n,m))