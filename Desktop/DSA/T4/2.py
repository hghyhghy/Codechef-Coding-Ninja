# Reverse digits of a number

def reverse_number(num):
    
    temp = int(str(num)[::-1])
    return temp

num=12345
print(reverse_number(num))