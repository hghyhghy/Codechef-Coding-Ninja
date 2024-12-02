

#longest substring with  k char

def main(array,k):

    n=len(array)
    maximum =float('-inf')

    for  i  in range(n):

        seen=set()

        for j in range(i,n):

            seen.add(array[j])

            if len(seen) > k:

                break

            maximum=max(maximum,j-i+1)

    return  maximum

s = "eceba"
k = 2

print(main(s,k))