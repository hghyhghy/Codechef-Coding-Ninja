

#triplet  with zero sum

def main(array):

    n=len(array)
    seen=set()

    for i in range(n):

        for j in range(i+1,n):

            for k in range(j+1,n):

                if array[i] + array[j] + array[k] == 0:

                    seen.add(tuple(sorted([array[i],array[j],array[k]])))


    return  list(seen) if seen else -1

arr = [-1, 0, 1, 2, -1, -4]
print(main(arr))
