#single number
from itertools import count


def main(array):

    freq={}

    for num in array:

        if num in freq:

            freq[num] +=1

        else:

            freq[num] =1


    number=[num for num,mount in freq.items() if mount ==1]

    return  number

a=[2 ,4 ,6 ,8 ,10 ,2 ,6 ,10]
print(main(a))