


#binary search

def main(array,target):

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

            right -= 1

    return  -1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

print(main(nums,target))
