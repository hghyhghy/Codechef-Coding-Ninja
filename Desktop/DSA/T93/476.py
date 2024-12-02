

#has pair with difference

def main(array,target):

    n=len(array)
    left=0
    right=1

    while right < n:

        difference = array[right] - array[left]

        if difference == target:

            return True

        elif difference < target:

            right +=1


        else:

            left +=1

        if left == right:

            right +=1

    return False


arr = [1, 2, 3, 4, 5]
K = 3
print(main(arr,K))

