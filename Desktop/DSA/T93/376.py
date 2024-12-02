

#rearrange positive and negative


def main(array):

    pos=[]
    neg=[]

    for num in array:

        if num > 0:

            pos.append(num)

        else:

            neg.append(num)

    i=0
    while pos and neg:

        array[i] = pos.pop(0)

        i +=1

        array[i] = neg.pop(0)

        i +=1

    return  array

arr = [1, -1, 2, -2, 3, -3]
print(main(arr))
