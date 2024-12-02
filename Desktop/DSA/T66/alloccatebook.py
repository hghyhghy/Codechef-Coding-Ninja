# Problem statement
# You have been given a number of stairs. Initially, you are at the 0th stair, and you need to reach the Nth stair.



# Each time, you can climb either one step or two steps.



# You are supposed to return the number of distinct ways you can climb from the 0th step to the Nth step.

def count_no_of_stairs(n):
    
    if n== 0:
        
        return 1
    
    if n ==1:
        
        return 1
    
    return count_no_of_stairs(n-1)+count_no_of_stairs(n-2)

n = 5
print(count_no_of_stairs(n))