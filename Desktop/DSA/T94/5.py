

#distinct in k sized window

def main(array,k):

    n=len(array)
    result=[]

    for i in range(n-k+1):

        distinct = set()

        for j in range(i,i+k):

            distinct.add(array[j])

        result.append(len(distinct))


    return  result

arr = [1, 2, 2, 1, 3, 1, 1, 3]
k = 4

print(main(arr,k))