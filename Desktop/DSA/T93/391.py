

#kth largest sum  subarray

def main(array:list[int],k:int):

    n=len(array)
    r=[]

    for i in range(n):

        current =0

        for j in range(i,n):

            current += array[j]

            r.append(current)


    r.sort(reverse=True)

    if k<n:

        return  r[k-1]

    else:

        return  -1


arr = [1, -2, 3, -4, 5]
K = 2

print(main(arr,K))