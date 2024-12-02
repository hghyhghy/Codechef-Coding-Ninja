

#maximum sum in circular subarray

def func(array):

    n=len(array)
    maximum=float("-inf")

    for i in  range(n):

        current  =0

        for j in range(i,i+n):

            current += array[j%n]

            maximum = max(maximum,current)

            if current < 0:

                current = 0

    return  maximum

arr = [1, 2, -3, -4, 5]
print(func(arr))

