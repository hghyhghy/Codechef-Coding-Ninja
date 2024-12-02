
#merge  k sorted array

def main(array):

    store=[]

    for num in array:

        store.extend(num)


    store.sort()

    return store

arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [0, 10, 11]
]

print(main(arrays))