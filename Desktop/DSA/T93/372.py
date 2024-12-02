

#minimum ;difference

def main(array):

    n=len(array)
    minimum=float("inf")

    for i in range(n):

        for j in range(i,n):

            difference = abs(array[i]-array[j])

            minimum=min(minimum,difference)

    return  minimum

arr = [3, -6, 7, -7, 0]
print(main(arr))