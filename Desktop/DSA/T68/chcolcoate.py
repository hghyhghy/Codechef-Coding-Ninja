# Given an array/list of integer numbers 'CHOCOLATES' of size 'N', where each value of the array/list represents the number of chocolates in the packet. There are ‘M’ number of students and the task is to distribute the chocolate to their students. Distribute chocolate in such a way that:

# 1. Each student gets at least one packet of chocolate.

# 2. The difference between the maximum number of chocolate in a packet and the minimum number of chocolate in a packet given to the students is minimum.

# Example :


def chocolate(array:list,m:int,n:int)->int:


    if m==0 or n==0:
        
        return 0
    
    array.sort()
    min_diff=float("inf")

    for i in range(n-m+1):
        
        diff= array[i+m-1] - array[i]

        min_diff=min(min_diff,diff)

    
    return min_diff

N = 5  # Number of packets
M = 3  # Number of students
chocolates = [8, 11, 7, 15, 2]

print(chocolate(chocolates,M,N))
    