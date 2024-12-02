

#search  in rotated sorted array

def main(array,target):

    n=len(array)

    for i in range(n):

        if array[i] == target:

            return  i

    return  -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(main(nums,target))