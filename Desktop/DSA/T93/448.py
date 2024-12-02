
#minimum subarray k size

def main(array,k):

    n=len(array)
    minimum=float('inf')

    for i in range(n-k+1):

        current=sum(array[i:i+k])

        if current < minimum:

            minimum = current

    return minimum


N = 7
K = 3
ARR = [2, 1, 5, 1, 3, 2, 1]
print(main(ARR,K))