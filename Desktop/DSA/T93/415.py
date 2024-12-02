
#container with most water

def main(array):

    n=len(array)
    left=0
    right=n-1

    max_area=0

    while left<right:

        width = right-left

        height=min(array[left],array[right])

        area=height*width

        max_area=max(max_area,area)

        if array[left]<array[right]:

            left +=1

        else:

            right -=1

    return max_area

A = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(main(A))