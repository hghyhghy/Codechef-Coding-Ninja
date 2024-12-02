


#shortest subarray

def shortest_subarray(string):

    n=len(string)
    seen=set(string)
    minimum=float("inf")
    result=""

    for i in range(n):

        for j in range(i+1,n+1):

            substring = string[i:j]

            if set(substring) == seen:

                if len(substring) <minimum:

                    minimum=len(substring)
                    result=substring
                    break

    return  result

S = "abcba"
print(shortest_subarray(S))



