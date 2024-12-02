

#subarray with  k distinct elements

def main(array,k):

    n=len(array)
    count =0

    for i  in range(n):

        seen=set()

        for j in range(i,n):

            seen.add(array[j])

            if len(seen) ==k:

                count +=1

            elif len(seen) > k:

                break

    return count

arr = [1, 2, 1, 2, 3]
K = 2

print(main(arr,K))