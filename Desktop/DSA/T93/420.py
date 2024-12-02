

#buy and sell stock

def main(array):

    n=len(array)
    maximum=0

    for i in range(1,n):

        if array[i]>array[i-1]:

            maximum += array[i]-array[i-1]


    return  maximum

prices = [7, 1, 5, 3, 6, 4]
print(main(prices))