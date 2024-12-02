

#sort the array by frequency

def main(array):

    freq={}
    first={}

    for  index,num  in enumerate(array):

        if num in freq:

            freq[num] +=1

        else:

            freq[num] =1
            first[num] = index



    new=sorted(array,key=lambda  x:(-freq[x],first[x]))

    return  new


arr = [2, 5, 2, 8, 5, 6, 8, 8]
print(main(arr))
