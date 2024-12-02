#subarray count

def main(array,k):

    n=len(array)
    count = 0

    for i in range(n):

        current = 0

        for  j in range(i,n):

            current += array[j]

            if current == k:

                count +=1

    return  count

arr = [3, 1, 2, 4]
K = 6

print(main(arr,K))