
#maximum of subarray

def main(array,k):

    n=len(array)
    result=[]

    for i in range(n-k+1):

        maximum=array[i]

        for j in range(i,i+k):

            if array[j] > maximum:

                maximum = array[j]


        result.append(maximum)


    return  result

arr = [1, 3, 1, 2, 0, 5]
K = 3

print(main(arr,K))

