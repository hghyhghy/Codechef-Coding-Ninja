

#top k frequent element

def main(array,k):

    freq={}

    for num in array:

        if num in freq:

            freq[num]+=1

        else:

            freq[num]=1


    new=sorted(freq,key=lambda x:freq[x],reverse=True)

    return  new[:k]

arr = [1, 2, 2, 3, 3]
k = 2

print(main(arr,k))