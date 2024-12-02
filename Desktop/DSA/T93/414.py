


#count subarray with k one

def main(array,k):

    n=len(array)
    result=0

    for i in range(n):

        count =0

        for j in range(i,n):

            if array[j] == 1:

                count +=1

            if count == k:

                result +=1

    return result

arr = [1, 0, 1]
k = 1

print(main(arr,k))





