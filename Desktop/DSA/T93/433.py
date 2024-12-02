

#squared num

def main(array:list[int]):

    new_array=[x**2 for x in array]

    new_array.sort()

    return  new_array

arr = [-6, -3, 2, 1, 5]
print(main(arr))