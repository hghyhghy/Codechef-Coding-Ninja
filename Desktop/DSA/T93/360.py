


#longest subarray with k elements

def main(array):

    n=len(array)
    maximum=float("-inf")

    for i in range(n):

        seen=set()

        for j in range(i,n):

            seen.add(array[j])

            if len(seen) > 2:

                break

            maximum=max(maximum,j-i+1)

    return  maximum

fruits = [1, 2, 1, 3, 2]
print(main(fruits))