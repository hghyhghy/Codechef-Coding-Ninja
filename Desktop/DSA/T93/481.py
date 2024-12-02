#majoritty element

def main(array):

    n=len(array)
    freq={}
    limit=n//2

    for num in array:

        if num in freq:

            freq[num]+=1

        else:

            freq[num]=1


    for num,count in freq.items():

        if count > limit:

            return  num


    return  -1

a=[2 ,3 ,9 ,2 ,2]
print(main(a))