# Write a program to input an integer 'n' and print the sum of all its even digits and the sum of all its odd digits separately.



# Digits mean numbers, not places! That is, if the given integer is "132456", even digits are 2, 4, and 6, and odd digits are 1, 3, and 5.

def sum_of_odd_even(number:int)->int:
    
    number_str=  str(number)
    
    odd=0
    even=0
    
    for num in number_str:
        
        if int(num)%2 == 0:
            
            even += int(num)
            
        elif int(num) %2 !=0:
            
            odd += int(num)
            
    return even,odd
    
        

a=430
print(sum_of_odd_even(a))