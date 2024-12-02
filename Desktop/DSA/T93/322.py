

#odd and even indexd element


def main(array):

    store1=[]
    store2=[]

    for num in array:

        if num % 2 == 0:

            store1.append(num)

        else:

            store2.append(num)

    return  sorted(store1)+sorted(store2)

nums=list(map(int,input().split()))
print(main(nums))

