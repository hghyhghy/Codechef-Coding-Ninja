# 2.	Find the Missing Number
# Input: [1, 2, 4, 6, 3, 7, 8]
# Expected Output : 5
# Explanation: Here the size of the array is 7, so the range will be [1, 8]. The missing number between 1 to 8 is 5


def missing_number(string):

    n=len(string)+1
    freq={num:True for num in string}

    for i in range(1,n+1):

        if i not in freq:

            return  i


    return -1


input_array = [1, 2, 4, 6, 3, 7, 8]
print(missing_number(input_array))