#  We are given an array of size n where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates.   There are m students, the task is to distribute chocolate packets such that: 

# Each student gets one packet.
# The difference between minimum and maximum selected packet is minimum.

def chocolate_distribution_problem(array,m):
    
    if not array or len(array) < m:
        
        return 0
    
    array.sort()
    min_difference= float('inf')
    n=len(array)
    
    for i in range(n-m+1):
        
        current_difference =  array[i+m-1] - array[i]
        min_difference = min(min_difference,current_difference)

    return min_difference

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

print(chocolate_distribution_problem(arr,m))
        
        