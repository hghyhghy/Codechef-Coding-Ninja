


#substring with k char

def main(string,k):

    n=len(string)
    maximum=float("-inf")

    for i in range(n):

        seen=set()

        for j in range(i,n):

            seen.add(string[j])

            if  len(seen) > k:

                break

            maximum=max(maximum,j-i+1)

    return  maximum

S = "bacda"
K = 3

print(main(S,K))