

#main

def main(array,target):

    n=len(array)
    minimum=float("inf")

    for  i  in range(n):

        current= 0

        for  j in range(i,n):

            current += array[j]

            if current > target:

                minimum=min(minimum,j-i+1)

                break

    return  minimum

arr = [1, 2, 21, 7, 6, 12]
X = 23

print(main(arr,X))