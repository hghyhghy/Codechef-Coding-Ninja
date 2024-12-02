

#majority

def main(array):

    n=len(array)
    freq={}
    limit=n/3
    r=[]

    for num in array:

        if num in freq:

            freq[num] += 1

        else:

            freq[num] = 1


    for num,count  in  freq.items():

        if count > limit:

            r.append(num)


    return  r

arr = [3, 1, 2, 2, 3, 3, 3, 4, 4]
print(main(arr))

