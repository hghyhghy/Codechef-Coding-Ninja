

#first non repeating char

def main(array):

    freq={}

    for num  in array:

        if num  in freq:

            freq[num] += 1

        else:

            freq[num] = 1

    for num,count in freq.items():

        if count  ==1:

            return  num


    return -1

arr = [4, 7, 3, 2, 7, 2]
print(main(arr))