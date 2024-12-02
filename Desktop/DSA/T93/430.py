
#maximum zeros
def main(array,k):

    n=len(array)
    maximum=float('-inf')

    for i in range(n):

        count =0

        for j in range(i,n):

            if  array[j] == 0:

                count+=1

            if count  > k:

                break

            maximum=max(maximum,j-i+1)

    return  maximum


