

#arrange alternatively

def main(array):

    pos=[x for x in array if x >  0]
    neg=[x for x  in array if x < 0 ]

    i=j=0
    r=[]

    while i < len(pos) and j < len(neg):

        r.append(neg[j])
        r.append(pos[i])

        j +=1
        i +=1

    if j<len(neg):

        r.append(neg[j])
        j +=1


    if i<len(pos):

        r.append(pos[i])
        i +=1



    return  r

print(main([4, -9, -2, 6, -8]))


