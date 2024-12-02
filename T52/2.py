# Given an array/list of integer numbers 'CHOCOLATES' of size 'N', where each value of the array/list represents the number of chocolates in the packet. There are ‘M’ number of students and the task is to distribute the chocolate to their students. Distribute chocolate in such a way that:

# 1. Each student gets at least one packet of chocolate.

# 2. The difference between the maximum number of chocolate in a packet and the minimum number of chocolate in a packet given to the students is minimum.

# Example :

def minimum_chocolate_to_distribute(array,m):
    
    n=len(array)

    if m==0 or n==0 or n<m:
        
        return 
    
    array.sort()
    minimum_difference=float('inf')

    
    for i in range(n-m+1):
        
        current_diff = array[i+m-1] - array[i]

        if current_diff < minimum_difference:
            minimum_difference = current_diff
            
    return minimum_difference

chocolates = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
M = 7

print(minimum_chocolate_to_distribute(chocolates,M))