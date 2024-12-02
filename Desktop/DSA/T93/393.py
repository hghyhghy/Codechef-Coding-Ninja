

#next greater element

def main(array):

    n=len(array)
    r=[-1]*n

    for i in range(n):

        for j in range(i+1,n):

            if array[j] > array[i]:

                r[i]=array[j]
                break

    return  r

arr = [1, 3, 2]
print(main(arr))


