#count subarray with zero sum


def main(array):

    n=len(array)
    count= 0

    for i in range(n):

        current =0

        for j in range(i,n):

            current += array[j]

            if current == 0:

                count +=1

    return  count

nums=list(map(int,input().split()))
print(main(nums))