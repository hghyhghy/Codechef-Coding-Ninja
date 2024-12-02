


#good subarray

def main(array,k):

    n=len(array)
    count =0

    for i in range(n):

        seen=set()

        for j in range(i,n):

            seen.add(array[j])

            if len(seen) == k:

                count += 1

            elif len(seen) > k:

                break

    return  count


arr = [1, 3, 1, 1, 2]
k = 2

print(main(arr,k))