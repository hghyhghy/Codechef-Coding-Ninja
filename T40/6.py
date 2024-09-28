# Problem statement
# Ninja is feeling very bored and wants to try something new. So, he decides to find the reverse of a given number. But he cannot do it on his own and needs your help.

# Note:

# If a number has trailing zeros, then its reverse will not include them. For e.g., the reverse of 10400 will be 401 instead of 00401.

def reverse_the_number(number):
    
    str_number=str(number)

    reversed_number=str_number[::-1]

    reversed_number = reversed_number.lstrip('0')

    node=int(reversed_number) if reversed_number else 0
    
    return node

number = 10400
print(reverse_the_number(number))