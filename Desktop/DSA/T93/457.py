

#single number

def main(array):

    freq={}

    for num in array:

        if num in freq:

            freq[num] +=1

        else:

            freq[num] =1


    for num,count in freq.items():

        if count ==1:

            return num


    return -1

a=[2,3,1,1,2,4]
print(main(a))