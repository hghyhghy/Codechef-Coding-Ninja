# The function accepts an integer array ‘arr’ of size ‘n’ as its argument. Each element of ‘arr’ represents the number of chocolates distributed to a person. The function needs to return the minimum number of chocolates that need to be distributed to each person so that the difference between the chocolates of any two people is minimized.

def chocolate_distrinution(arr):

    if len(arr) < 2:

        return 0
    
    arr.sort()

    max_value=arr[-1] + arr[0] + 1
    min_difference= max_value

    for i in range(len(arr)-1):

        diff = arr[i+1] - arr[i]

        if diff < min_difference:

            min_difference = diff

    
    return min_difference + 1

arr = [7, 3, 1, 9, 5]
print(chocolate_distrinution(arr))