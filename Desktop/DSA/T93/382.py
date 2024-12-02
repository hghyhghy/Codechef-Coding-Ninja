

#water with maximum water

def main(array:list[int])->int:

    n=len(array)
    left=0
    right=n-1
    maximum=float("-inf")

    while left < right:

        height=min(array[left],array[right])

        width = right-left

        area =  height * width

        maximum=max(maximum,area)

        if array[left] < array[right]:

            left +=1

        else:

            right -=1

    return  maximum

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(main(arr))
