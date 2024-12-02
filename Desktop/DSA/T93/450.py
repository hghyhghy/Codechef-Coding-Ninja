


#longest subarray with k sum

def main(array,k):

    n=len(array)
    maximum=float('-inf')

    for i in range(n):

        current = 0

        for j in range(i,n):

            current += array[j]

            if current == k:

                length =j-i+1

                maximum=max(maximum,length)

    return  maximum

N = 5
K = 4
NUMS = [1, 2, 1, 0, 1]

print(main(NUMS,K))