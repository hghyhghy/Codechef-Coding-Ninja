

#duplicate element

def main(array):

    freq={}

    for num in array:

        if num in freq:

            return  num

        else:

            freq[num]=1


    return -1

a=[1,1,5,6,3,3,0]
print(main(a))