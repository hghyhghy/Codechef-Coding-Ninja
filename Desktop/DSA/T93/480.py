

#binary search

def main(array,target):

    n=len(array)
    left=0
    right=n-1

    while left <= right:

        mid=(left+right)//2

        if array[mid] == target:

            return mid

        elif array[mid] < target:

            left = mid +1

        else:

            right = mid - 1

    return 0

a=[1 ,2 ,3 ,4 ,5]
print(main(a,4))