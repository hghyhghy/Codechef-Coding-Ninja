# You are given two non-negative integers, ‘NUM1’ and ‘NUM2’, in the form of strings. Return the sum of both strings.

def sum_of_strings(num1,num2):
    
    i1=int(num1)
    i2=int(num2)

    total =  i1+i2
    
    return str(total)

num1 = "123"
num2 = "456"
print(sum_of_strings(num1,num2))