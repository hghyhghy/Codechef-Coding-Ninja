

#duplicate at the distance k

def func(array,k):

    n=len(array)
    for i in range(n):

        for j in range(i+1,min(i+k+1,n)):

            if array[i] == array[j]:

                return  True

    return  False

arr = [1, 2, 3, 1, 2, 3]
k = 3

print(func(arr,k))