

#maximum from  k sized subarray

def main(array,k):

    n=len(array)
    r=[]

    for i in range(n-k+1):

        subarray=array[i:i+k]

        maximum=max(subarray)

        r.append(maximum)

    return r

A = [3, 2, 3, 5, 1, 7]
K = 3

print(main(A,K))