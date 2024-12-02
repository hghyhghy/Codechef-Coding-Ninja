

#finding intersection

def main(a1,n,a2,m):

    i=j=0
    r=[]

    while i<n and j<m:

        if a1[i] == a2[j]:

            r.append(a1[i])

            i +=1
            j +=1

        elif a1[i] < a2[j]:

            i +=1

        else:

            j +=1

    return  r

arr = [1, 2, 4, 5, 6]
brr = [2, 3, 5, 7]
n = len(arr)
m = len(brr)
print(main(arr,n,brr,m))