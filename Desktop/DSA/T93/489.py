#next greater element

def main(array):

    n=len(array)
    dp=[-1]*n

    for i in range(n):

        for j in range(i+1,n):

            if array[j]> array[i]:

                dp[i]=array[j]
                break

    return  dp

arr = [4, 5, 2, 25]
print(main(arr))