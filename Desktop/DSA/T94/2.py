#index of the two sum

def main(array,target):

    n=len(array)

    result= (-1,-1)

    for i in range(n):

        for j in range(i+1,n):

            if array[i]+ array[j] == target:

                result=(i,j)


    return  result

Arr = [1, 3, 2, 4, 6]
target = 6

print(main(Arr,target))

