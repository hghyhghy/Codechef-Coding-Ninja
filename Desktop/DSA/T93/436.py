
#maximum length

def main(array):

    n=len(array)
    maximum =float("-inf")

    for i  in range(n):

        current = 0

        for j in range(i,n):

            current += array[j]

            if current == 0:

                maximum = max(maximum,j-i+1)

    return  maximum

arr = [1, -1, 3, 2, -2, -3, 3]
print(main(arr))