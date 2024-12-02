

#first one

def main(array,n):

    left=0
    right = n-1

    first =-1

    while left <= right:

        mid =(left+right)//2

        if array[mid] == 1:

            first = mid
            right = mid-1

        else:

            left = mid +1

    return  first+1

a=[2,3,1,4,5]
print(main(a,5))