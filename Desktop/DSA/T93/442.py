

#occurance if the number

def main(array,x):

    freq={}

    for num in array:

        if num in freq:

            freq[num] +=1

        else:

            freq[num] = 1


    if x in  freq:

        return  freq.get(x,0)

    else:

        return  0

a=[2,1,3,5,6,0,9,0]
print(main(a,0))