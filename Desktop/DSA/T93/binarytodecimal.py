#binary to decimal
def b_d(number):
    
    return int(number,2)

def d_b(number):
    
    return bin(number)[2:]

binary = input("Enter a binary number: ")
decimal = b_d(binary)
print(f"The decimal equivalent of {binary} is {decimal}")

decimal = int(input("Enter a decimal number: "))
binary = d_b(decimal)
print(f"The binary equivalent of {decimal} is {binary}")