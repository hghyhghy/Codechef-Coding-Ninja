
#cyclically rotate array

def main(array):

    n=len(array)
    last=array[-1]

    for i in  range(n-1,-1,-1):

        array[i]=array[i-1]


    array[0]=last

    return  array

arr1 = [1, 2, 3, 4, 5]
print(main(arr1))