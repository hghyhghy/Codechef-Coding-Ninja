
#consecutive element
def main(array:list[int]):

    array.sort()

    n=len(array)
    for i in range(1,n):

        if array[i] - array[i-1] != 1:

            return False

    return  True

arr = [4, 3, 5]
print(main(arr))

