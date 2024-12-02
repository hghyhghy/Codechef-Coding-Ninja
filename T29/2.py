# You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.

# Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.

# Your task is to find the missing number (M) and the repeating number (R).

# For example:
# Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
# The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) and 5 is the repeating number (R). 

def repeating_number(arr):
    
    freq={}

    for num in arr:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    
    result=[num for num,count in freq.items() if count > 1]

    return result,len(arr)

def missing_number(arr):
    # Sort the array in place
    arr.sort()

    # Compute the length of the sorted array
    n = len(arr)

    # Calculate the expected sum of the first n numbers
    expected_sum = (n * (n + 1)) // 2

    # Calculate the actual sum of the array
    actual_sum = sum(arr)

    # The missing number is the difference between the expected sum and the actual sum
    missing = expected_sum - actual_sum

    return missing

# Example usage
arr = [4, 3, 2, 7, 8, 1, 5]
print(missing_number(arr))



arr = [4, 3, 2, 7, 8, 2, 1, 5]
print(repeating_number(arr))