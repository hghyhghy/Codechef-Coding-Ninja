
#maximum xor operation

def func(array):

    n=len(array)
    maximum=float("-inf")


    for i in range(n):

        for j in range(i+1,n):

            xor=array[i]^array[j]

            maximum=max(maximum,xor)

    return  maximum

arr = [2, 5, 6]
print(func(arr))