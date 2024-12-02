

#max count of zero

def func(array):

    n=len(array)
    count =0
    maximum=0

    for i in range(n):

        if array[i] == 0:

            count +=1

        else:

            maximum=max(maximum,count)
            count =0

    maximum=max(maximum,count)
    return  maximum

array = [1, 0, 0, 1, 0, 0, 0, 1, 0]
print(func(array))
