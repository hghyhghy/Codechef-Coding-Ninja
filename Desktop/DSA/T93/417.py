

#four sum

def main(array,target):

    n=len(array)
    seen=set()

    for i in range(n):

        for j in range(i+1,n):

            for k in range(j+1,n):

                for l in range(k+1,n):

                    if array[i]+array[j]+array[k]+array[l] == target:

                        seen.add(tuple(sorted([array[i],array[j],array[k],array[l]])))


    return  list(seen) if seen else -1

arr = [1, 0, -1, 0, -2, 2]
target = 0

print(main(arr,target))