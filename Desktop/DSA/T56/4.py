# You are given an array/list ‘BINARYNUMS’ that consists of ‘N’ distinct strings which represent all integers from 0 to N in binary representation except one integer. This integer between 0 to ‘N’ whose binary representation is not present in list ‘BINARYNUMS’ is called ‘Missing Integer’.

# Your task is to find the binary representation of that ‘Missing Integer’. You should return a string that represents this ‘Missing Integer’ in binary without leading zeros.

# Note

# 1. There will be no leading zeros in any string in the list ‘BINARYNUMS’.
# Example:

# Consider N = 5 and the list ‘binaryNums’=  [“0”, “01”, “010”, “100”, “101”].  This list consists of the binary representation of numbers [0, 1, 2, 4, 5]. Clearly, the missing number is 3 and its binary representation will be “11”. So you should return string “11”.

def find_the_missing_number(array):
    
    n=len(array)
    expecteD_sum =n*(n+1)//2
    
    actual_sum = sum(array)

    missing = expecteD_sum-actual_sum
    
    return missing

print(find_the_missing_number([9,6,4,2,3,5,7,0,1]))