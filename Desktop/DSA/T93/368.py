

#max profit on day 2

def main(array):

    n=len(array)
    maximum=float("-inf")

    for i in range(n):

        for j in range(i+1,n):

            profit = array[j]-array[i]

            if profit >  0:

                remaining = 0

                for  k in range(j+2,n):

                    for l in range(k+1,n):

                        remaining=max(remaining,array[l]-array[k])


                maximum=max(maximum,remaining+profit)

    return  maximum

prices = [3 ,7 ,7 ,1 ,3 ,8 ,4 ,4 ,8 ,10 ]
print(main(prices))