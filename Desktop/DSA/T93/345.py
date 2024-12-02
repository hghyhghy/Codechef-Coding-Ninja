

#kadanes algorithm mximum subarray sum

def func(array):

    total=0
    maximum=float("-inf")

    for num in array:

        total += num

        if total > maximum:

            maximum=total

        if total < 0:

            total = 0

    return  maximum

ARR = [1, 2, -3, 4, 5]
print(func(ARR))