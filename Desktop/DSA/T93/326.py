

#max consecutive one
def main(array):

    n=len(array)
    maximum=float("-inf")
    count=0

    for i in range(n):

        if array[i] == 1:

            count +=1

        else:

            maximum=max(maximum,count)
            count =0

    maximum=max(maximum,count)
    return  maximum

nums = [1, 1, 0, 1, 1, 1]
print(main(nums))