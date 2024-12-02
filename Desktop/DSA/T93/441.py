

#moving zero to end

def main(array):

    zero=[]
    none_zero=[]

    for num in array:

        if num == 0:

            zero.append(num)

        else:

            none_zero.append(num)

    return  none_zero+zero


arr = [0, 1, -2, 3, 4, 0, 5, -27, 9, 0]
print(main(arr))