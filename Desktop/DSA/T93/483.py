

#kth largest and smallest

def main(array,k):

    largest=-1
    smallest=-1

    new=sorted(array)
    smallest=new[k-1]

    new1=sorted(array,reverse=True)
    largest=new1[k-1]

    return largest,smallest

a=[34,21,3,1,89]
k=2

print(main(a,k))