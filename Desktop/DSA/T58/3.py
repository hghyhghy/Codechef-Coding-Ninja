# 402. Remove K Digits
# Medium
# Topics
# Companies
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

def smallest_after_k_elements_removal(array,k):
    
    
    stack=[]
    
    for num in array:
        
        while k>0 and stack and stack[-1] > num:
            
            stack.pop()
            k -=1
            
        stack.append(num)
        
    final = stack[:-k] if k else stack
    
    result = ''.join(final).lstrip("0")

    return result if result else None

print(smallest_after_k_elements_removal("1432219",3))