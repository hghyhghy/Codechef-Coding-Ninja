

#negative in every k sized window

def func(array,k):

    n=len(array)
    result=[]

    for i in range(n-k+1):

        negative=0

        for j in range(i,i+k):

            if array[j] <  negative:

                negative = array[j]
                break

        result.append(negative)

    return  result

arr = [5, -3, 2, 3, -4]
k = 2

print(func(arr,k))