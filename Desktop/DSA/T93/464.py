

#pair with given sum


def main(array,target):

    n=len(array)
    count  = 0

    for i in range(n):

        for j in range(i+1,n):

            if array[i] + array[j] ==  target:

                count +=1

    return  count


arr = [1, 2, 3, 4, 3]
Sum = 6

print(main(arr,Sum))