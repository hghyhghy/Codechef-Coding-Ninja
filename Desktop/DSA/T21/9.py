# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

def canshift(string,goal):
    
    if len(string) != len(goal):
        
        return True
    
    concatenated= string + string
    
    return goal in concatenated

s = "abcde"
goal = "cdeab"

print(canshift(s,goal))