

#find the last element

def main(array,target):

    n=len(array)
    last=-1


    for  i in range(n-1,-1,-1):

        if array[i] == target:

            last=i
            break

    return  last

arr = [1, 2, 3, 2, 5, 2, 7]
x = 2

print(main(arr,x))