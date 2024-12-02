
#merge two sorted array

def main(arr1,arr2,m,n):

    i=m-1
    j=n-1
    k=m+n-1

    while i>=0 and j>=0:

        if arr1[i]>arr2[j]:

            arr1[k]=arr1[i]

            i -=1

        else:

            arr1[k]=arr2[j]

            j -=1

        k -=1


    while j>=0:

        arr1[k]=arr1[i]
        j -=1
        k -=1

    return  arr1

ARR1 = [1, 3, 5, 0, 0, 0]  # First list with extra space
ARR2 = [2, 4, 6]  # Second list
m = 3  # Number of valid elements in ARR1
n = 3

print(main(ARR1,ARR2,m,n))