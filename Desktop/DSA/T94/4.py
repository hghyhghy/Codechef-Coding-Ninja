
#common element


def main(arr1,arr2):

    common=[]
    store = arr1[:]

    for num in arr2:

        if num in store:

            common.append(num)
            store.remove(num)

    return  common

arr1 = ["ab", "dc", "ab", "ab"]
arr2 = ["dc", "ab", "ab"]

print(main(arr1,arr2))