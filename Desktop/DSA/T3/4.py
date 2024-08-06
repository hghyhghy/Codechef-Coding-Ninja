# Implement the function:

# Int SquareRootDifference(int m, int n);

# Calculate and return the difference between the sum of square roots of even numbers and the sum of square roots of odd numbers in the range from ‘m’ to ‘n’ (inclusive).

def difference(m,n):
    
    odd=0
    even=0
    
    for i in range(m,n+1):
        
        if i %2  ==0:
            
            even += (i**2)
            
        elif  i %2 !=0:
            
            odd += (i**2)
            
    return abs(even - odd)

print(difference(1,10))