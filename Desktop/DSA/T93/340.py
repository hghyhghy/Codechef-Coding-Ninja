

#minimum in rotated sorted array

def func(array):

    n=len(array)
    minimum=array[0]

    for i in range(n):

        if array[i] < minimum:

            minimum=array[i]

    return minimum

nums = [3,4,5,1,2]
print(func(nums))