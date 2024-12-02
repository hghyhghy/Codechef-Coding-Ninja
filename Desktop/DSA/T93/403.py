

#subarray with target xor


def main(array,target):

    n=len(array)
    count =0

    for i in range(n):

        current= 0

        for j in range(i,n):

            current ^= array[j]

            if current ==  target:

                count += 1

    return  count

arr = [1, 2, 3, 4]
X = 3

print(main(arr,X))
