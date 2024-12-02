

#smallest than triplet

def main(array,target):

    n=len(array)
    count=0

    for i in range(n):

        for j in range(i+1,n):

            for k in range(j+1,n):

                if array[i]+array[j]+array[k] < target:

                    count +=1

    return count

arr = [1, 5, 2, 3, 4, 6, 7]
target = 9

print(main(arr,target))


