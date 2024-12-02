


#two sum

def main(array,target):

    n=len(array)
    left=0
    right=n-1

    while left < right:

        current=array[left]+array[right]

        if current == target:

            return  left,right

        elif current < target:

            left +=1

        else:

            right -= 1

    return  -1

arr = [1, 2, 3, 4, 5]
target = 8

print(main(arr,target))