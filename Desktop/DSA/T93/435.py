

#buy sell stokc

def main(array):

    minimum=float('inf')
    maximum=0

    for num in array:

        if num < minimum:

            minimum =  num

        profit = num-minimum

        if profit > maximum :

            maximum = profit


    return  maximum

prices = [7, 1, 5, 3, 6, 4]
print(main(prices))