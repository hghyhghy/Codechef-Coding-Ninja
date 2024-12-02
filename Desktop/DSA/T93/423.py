

#majority element

def main(array,k):

    n=len(array)
    limit=n//k

    freq={}
    for num in array:

        if num in freq:

            freq[num] +=1

        else:
            freq[num] =1

    r=[]

    for num,count in freq.items():

        if count >= limit:

            r.append(num)

    return  r

arr = [1, 2, 3, 3, 3, 3, 4, 4, 4, 1, 2, 0]
k = 4

print(main(arr,k))