
#kth smallest element

def bubble_sort(array):

    n=len(array)

    for i in range(n):

        for j in range(0,n-i-1):

            if array[j]>array[j+1]:

                array[j],array[j+1]=array[j+1],array[j]

    return  array

def main(array,k):

    temp=bubble_sort(array)

    return  temp[k-1]


arr = [12, 3, 5, 7, 19]
print(main(arr,2))