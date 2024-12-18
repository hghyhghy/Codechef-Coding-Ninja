# Problem statement
# You are given two numbers 'A' and 'B' in the form of two arrays (A[] and B[]) of lengths 'N' and 'M' respectively, where each array element represents a digit. You need to find the sum of these two numbers and return this sum in the form of an array.

# Note:

# 1. The length of each array is greater than zero.

# 2. The first index of each array is the most significant digit of the number. For example, if the array A[] = {4, 5, 1}, then the integer represented by this array is 451 and array B[] = {3, 4, 5} so the sum will be 451 + 345 = 796. So you need to return {7, 9, 6}.

# 3. Both numbers do not have any leading zeros in them. And subsequently, the sum should not contain any leading zeros

def sum_of_two_arrays(a1,a2):
    
    if len(a1) != len(a2):
        
        return None
    
    result=[0]*len(a1)

    for i in range(len(a1)):
        
        result[i] = a1[i] + a2[i]

    
    return result

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

print(sum_of_two_arrays(arr1,arr2))