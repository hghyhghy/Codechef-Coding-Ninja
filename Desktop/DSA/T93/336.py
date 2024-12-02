

#best time to buy and sell stock

def func(array):

    n=len(array)
    maximum=0

    for i in range(n):

        for j in range(i+1,n):

            profit=array[j]-array[i]
            maximum=max(maximum,profit)


    return  maximum

prices = [7, 1, 5, 3, 6, 4]
print(func(prices))