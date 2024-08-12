# An accountant in a firm has a serious issue with numbers, He types the numbers in a reverse manner. Suppose he has to enter 123, he enters the number 321. He has the habit of reading numbers from right to left.
# The boss became aware of this only after he found out at the end of the billing month when he had to file the tax. He has to correct all the numbers by reentering each number from right to left. This gives the corrected number.
# Given a number N, help the boss find out the corrected numbers. Display the corrected numbers as output. Also, ignore any 0's at the end of the number.
# Note: The corrected numbers should be only 16-bit signed integers. If the output number is outside the range display "Wrong Value"

def corrected_number(n):
    
    reversed_string=str(n)[::-1]

    corrected_string = reversed_string.lstrip('0')

    if corrected_string == "":
        
        corrected_string ="0"
        
    corrected_int= int(corrected_string)

    minimum=-32768
    maximum=32767
    
    if minimum <= corrected_int <= maximum:
        
        return corrected_int
    
    else:
        
        return 'Invalid'

number = int(input("Enter a number: "))
result = corrected_number(number)
print(result)
