# Problem statement
# You are given two numbers 'A' and 'B' in the form of two arrays (A[] and B[]) of lengths 'N' and 'M' respectively, where each array element represents a digit. You need to find the sum of these two numbers and return this sum in the form of an array.

# Note:

# 1. The length of each array is greater than zero.

# 2. The first index of each array is the most significant digit of the number. For example, if the array A[] = {4, 5, 1}, then the integer represented by this array is 451 and array B[] = {3, 4, 5} so the sum will be 451 + 345 = 796. So you need to return {7, 9, 6}.

# 3. Both numbers do not have any leading zeros in them. And subsequently, the sum should not contain any leading zeros
# using pointers 

def add_two_arrays(arr1,arr2):
    
    pointer1=0
    pointer2=0
    
    result=[]

    while pointer1 < len(arr1) and pointer2 < len(arr2):
        
        store = (arr1[pointer1] + arr2[pointer2])
        result.append(store)

        pointer1 += 1
        pointer2 += 1
        
    return result

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(add_two_arrays(arr1,arr2))