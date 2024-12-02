

#common

def func(arr1,arr2):

    commom=[]
    store=arr1[:]

    for char in arr2:

        if char in store:

            commom.append(char)
            store.remove(char)

    return  commom

arr1 = ["ab", "dc", "ab", "ab"]
arr2 = ["dc", "ab", "ab"]

print(func(arr1,arr2))