# Problem statement
# Given an array of length N, you need to find and print the sum of all elements of the array.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 10^6
# Note for C++:
# It is advisable to declare an array with a size that can accommodate all the elements, considering that N has a maximum value of 10^5

def sum_of_the_elements_of_array(array):
    
    temp_store=0

    for num in (array):
        
        temp_store += num

    return temp_store

a=[9 ,8 ,9]
print(sum_of_the_elements_of_array(a))