
#count pair with sum zero

def main(array):

    n=len(array)
    count =0

    for i in range(n):

        for j in range(i+1,n):

            if array[i] + array[j] == 0:

                count +=1

    return  count


arr = [2, -2, 3, -3, 4, -4, 0]
print(main(arr))