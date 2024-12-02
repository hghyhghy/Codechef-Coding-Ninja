

#find pair with given sum

def  main(array,target):

    n=len(array)
    count= 0

    for i in range(n):

        for j in range(i+1,n):

            if array[j]-array[i]==target:

                count  +=1

    return  count

arr = [1, 5, 2, 1, 3, 4, 2]
K = 2
print(main(arr,K))
