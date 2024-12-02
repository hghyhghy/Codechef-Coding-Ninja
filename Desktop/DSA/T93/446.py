
#common element

def main(a1,a2,a3):

    i=j=k=0
    r=[]

    while i<len(a1) and j<len(a2) and k<len(a3):

        if a1[i]==a2[j]==a3[k]:

            if not r or r[-1] != a1[i]:

                r.append(a1[i])

            i +=1
            j +=1
            k +=1


        elif a1[i]<a2[j]:

            i += 1

        elif a2[j]<a3[k]:

            j +=1

        else:

            k +=1

    return  r

A = [2, 3, 4, 7]
B = [0, 0, 3, 5]
C = [1, 3, 8, 9]

print(main(A,B,C))