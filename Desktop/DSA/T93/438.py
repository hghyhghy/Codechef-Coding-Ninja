

#move zeroes

def main(array):

    n=len(array)
    zero=0

    for i in range(n):

        if array[i] != 0:

            array[zero],array[i]=array[i],array[zero]

            zero +=1



    return  array

arr = [0, 1, -2, 3, 4, 0, 5, -27, 9, 0]
print(main(arr))

