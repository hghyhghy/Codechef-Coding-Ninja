

#zero to left

def main(array):

    n=len(array)
    zero=n-1

    for i in range(n-1,-1,-1):

        if array[i] != 0:

            array[zero] =array[i]
            zero -=1


    while zero >=0:

        array[zero]=0
        zero -=1


    return array

arr = [1, 1, 0, 2, 0]
print(main(arr))