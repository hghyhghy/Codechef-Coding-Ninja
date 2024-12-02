from T76.buysellstock import prices


#best time to buy and eell stock

def main(array):

    n=len(array)
    maximum=0

    for i in range(n-1):

        if array[i+1] > array[i]:

            maximum += array[i+1] - array[i]

    return  maximum

PRICES = [7, 1, 5, 4, 3, 6]
print(main(PRICES))