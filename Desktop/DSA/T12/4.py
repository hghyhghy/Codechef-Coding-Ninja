# Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

# Note: There are no duplicates in the list.

def missing_number(array,n):
    
    expected_sum=n*(n+1)//2

    total_sum=sum(array)

    missing_element= expected_sum - total_sum

    return missing_element

arr = [1, 2, 4, 5, 6]  # Example array with missing number 3
N = 6  # Since the array contains numbers from 1 to 6

print(missing_number(arr,N))