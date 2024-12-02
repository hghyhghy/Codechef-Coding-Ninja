# missing number from the array

def missing_number_from_array(array):
    
    n=len(array)+1
    expected_sum = n*(n+1)//2
    
    actual_sum = sum(array)

    return expected_sum - actual_sum

arr = [1, 2, 4, 5, 6]
print(missing_number_from_array(arr))