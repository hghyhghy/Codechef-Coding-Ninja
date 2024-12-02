

#missing number from the array

def main(array):

    freq={}

    for num in array:

        freq[num] = True

        for i in range(1,len(array)+1):

            if i not in freq:

                return  i

    return -1

a=[1,2,4,5]
print(main(a))