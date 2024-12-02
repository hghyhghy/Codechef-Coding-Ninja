

#minimumin rotated sorted array

def main(array):

    if not array:

        return  array

    minimum=array[0]

    for num in array:

        if num < minimum:

            minimum = num

    return  minimum

arr = [4, 5, 6, 1, 2, 3]
print(main(arr))

