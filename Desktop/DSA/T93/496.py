
#product of array except itself

def main(array):

    n=len(array)
    dp=[-1]*n

    for i in range(n):

        product =1

        for j in range(i+1,n):

            if i != j:

                product *= array[j]


        dp[i]= product


    return dp

a=[1,2,3,4]
print(main(a))

