

#occurance of the number

def main(array,target):

    freq={}

    for num in array:

        if  num in freq:

            freq[num] +=1

        else:

            freq[num] = 1


    return freq.get(target,0)

arr = [1, 1, 2, 2, 2, 3, 3, 4]
x = 2
print(main(arr,x))