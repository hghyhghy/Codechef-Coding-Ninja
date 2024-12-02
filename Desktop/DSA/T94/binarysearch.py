

#binary search

def binary_search(array,target):

    n=len(array)
    left=0
    right=n-1

    while left < right:

        mid=(left+right)//2

        if array[mid] == target:

            return  mid

        elif array[mid] < target:

            left +=1

        else:

            right -=1

    return  -1

arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
print(binary_search(arr,100))