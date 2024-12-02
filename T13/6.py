# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

def add_strings(num1,num2):
    
    i=len(num1) - 1
    
    j=len(num2) - 1
    
    carry = 0
    
    result=[]
    
    while i >=0 or j>=0 or carry:
        
        digit1=int(num1[i]) if i>=0 else 0
        digit2=int(num2[j]) if j>=0 else 0
        
        total = digit1 + digit2 + carry
        
        carry = total//10
        
        result.append(total%10)

        i -= 1
        j -= 1
        
        
    return "".join(str(digit) for digit in reversed(result))

num1 = "123"
num2 = "456"

print(add_strings(num1,num2))

        
        