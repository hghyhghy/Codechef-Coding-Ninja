from adodbapi.apibase import cvtUnicode


#product less than k

def main(array,k):

    n=len(array)
    count=0

    for i in range(n):

        product = 1

        for j in range(i,n):

            product *= array[j]

            if product < k:

                count +=1

            else:

                break

    return  count


arr = [1, 2, 3, 4, 5]
k = 7

print(main(arr,k))