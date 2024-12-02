

#first and last position of the array

def main(array,target):

    n=len(array)
    first=-1
    last=-1

    for i in range(n):

        if array[i] == target:

            first=i
            break


    for j  in range(n-1,-1,-1):

        if array[j] == target:

            last=j
            break

    return  first,last


arr = [1, 2, 4, 4, 5]
x = 4

print(main(arr,x))