

#maximum product of subarray

def main(array):

    n=len(array)
    maximum=float("-inf")

    for i in range(n):

        product = 1

        for j in range(i,n):

            product *=  array[j]

            maximum=max(maximum,product)

    return  maximum

arr = [2, 3, -2, 4]
print(main(arr))