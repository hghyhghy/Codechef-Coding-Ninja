# Problem statement
# You are given two non-negative numbers 'num1' and 'num2' represented in the form of linked lists.



# The digits in the linked lists are stored in reverse order, i.e. starting from least significant digit (LSD) to the most significant digit (MSD), and each of their nodes contains a single digit.



# Calculate the sum of the two numbers and return the head of the sum list.

def sum_of_elements_of_array(arr1,arr2):
    
    result=sum(arr1)

    result1=sum(arr2)

    return result+result1

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

print(sum_of_elements_of_array(arr1,arr2))