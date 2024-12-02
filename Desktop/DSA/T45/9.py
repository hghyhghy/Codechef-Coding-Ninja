# Problem statement
# You are given an array/list ‘BINARYNUMS’ that consists of ‘N’ distinct strings which represent all integers from 0 to N in binary representation except one integer. This integer between 0 to ‘N’ whose binary representation is not present in list ‘BINARYNUMS’ is called ‘Missing Integer’.

# Your task is to find the binary representation of that ‘Missing Integer’. You should return a string that represents this ‘Missing Integer’ in 
# binary without leading zeros.

def missing_number(array):
    
    n=len(array)

    expected_sum  = (n+1)*(n+2) // 2
    
    actual_sum =  sum(array)

    midding = expected_sum - actual_sum
    
    return midding

arr = [1, 2, 4, 5, 6] 
print(missing_number(arr))

