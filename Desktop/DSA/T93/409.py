

#subsarray with given sum

def main(array,target):

    n=len(array)


    for i in range(n):

        current= 0

        for j in range(i,n):

            current += array[j]

            if current == target:

                return [i,j]

    return -1

ARR = [1, 2, 3, 4]
S = 7

print(main(ARR,S))

