

#best time to buy and sell stock

def main(array,fees):

    minimum=float("inf")
    maximum=0


    for num in array:

        minimum=min(minimum,num)

        profit=(num-minimum) + fees

        maximum=max(maximum,profit)


    return  maximum

prices1 = [3, 4, 5, 63, 3, 6]
fee1 = 1

print(main(prices1,fee1))