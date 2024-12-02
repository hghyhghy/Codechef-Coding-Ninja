


#count with k different substring

def main(array,k):

    n=len(array)
    count= 0

    for i in range(n):

        for j in range(i,n):

            new=array[i:j+1]

            distinct=set(new)

            if len(distinct) == k:

                count +=1

    return  count

s = "abcad"
k = 2

print(main(s,k))