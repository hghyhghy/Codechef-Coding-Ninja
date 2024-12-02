

#shortest subarray with minimum length

def main(array,k):

    n=len(array)
    minimum=float("inf")

    for start in range(n):

        temp = 0

        for end in range(start,n):

            temp += array[end]

            if temp >= k:

                minimum=min((minimum,end-start+1))

                break

    return  minimum

nums = [1, 2, 3, 4, 5]
k = 11

print(main(nums,k))

