


#maximum product element

def func(array):

    n=len(array)
    maximum=float("-inf")

    for i in range(n):

        product = 1

        for j in range(i,n):

            product *= array[j]

            maximum=max(maximum,product)

    return maximum

nums = [2,3,-2,4]
print(func(nums))