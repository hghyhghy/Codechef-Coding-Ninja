
#buy and sell  stock

def main(array):

    maximum =0
    minimum=float('inf')

    for num in array:

        if num < minimum:

            minimum = num

        profit  =  num-minimum

        maximum=max(maximum,profit)


    return  maximum

a=[ 2, 100, 150, 120]
print(main(a))