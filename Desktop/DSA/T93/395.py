

#smallest subarray with k char

def main(string,k):

    n=len(string)
    first=last=-1
    minimum= float("-inf")

    for i in range(n):

        seen=set()

        for j in range(i,n):

            seen.add(string[j])

            if len(seen) == k:

                length =j-i+1

                if length < minimum:

                    first=i
                    end=j
                    minimum=length

                    break


    return string[first:last+1]


arr = [1, 2, 2, 3, 1, 3]
K = 2

print(main(arr,K))
