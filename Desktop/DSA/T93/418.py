

#maximum distance

def main(array):

    n=len(array)
    maximum=float("-inf")

    for i in range(n):

        for j in range(i,n):

            if array[i]<=array[j]:

                temp=array[j]-array[i]

                maximum=max(maximum,temp)

    return  maximum

A = [3, 5, 4, 1]
print(main(A))