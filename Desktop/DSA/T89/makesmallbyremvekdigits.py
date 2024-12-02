# You are given a non-negative integer ‘num’ in the form of a string and provided with an integer ‘k’.



# You need to find the smallest integer possible by removing exactly ‘k’ digits from ‘num.’



# Note :
# ‘num’ does not have leading zeros except when ‘num’ equals zero.
# Example:
# Input: ‘num’ = ‘141’ , ‘k’ = 1.

# Output: ‘11’

# Explanation: By removing only 1 digit from ‘num’, 3 numbers can be formed: 14, 11, and 41. Out of which 11 is the smallest number.
# Note :
# You don’t have to print anything. It has already been taken care of. Just implement the given function.

def smallest_after_k_removal(num:str,k:int)->str:
    
    n=len(num)
    smallest=None
    
    
    if k>=n:
        
        return '0'

    
    for i in range(n-k+1):
        
        new_num = num[:i]+num[i+1:]

        new_num = new_num.lstrip("0")

        if new_num == " ":
            
            return "0"

        if smallest is None or  int(new_num) < int(smallest):
            
            smallest = new_num
            
    
    return smallest

num = '141'
k = 1

print(smallest_after_k_removal(num,k))