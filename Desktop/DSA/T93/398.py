#longest continous

def main(array):

    n=len(array)
    maximum=float("-inf")

    def check(arr:list[int]):

        arr.sort()

        for i in range(1,len(arr)):

            if arr[i]-arr[i-1] != 1:

                return  False


        return  True


    for i in range(n):

        for j in range(i,n):

            substring=array[i:j+1]

            if check(substring):

                maximum=max(maximum,len(substring))

    return  maximum

arr = [1, 2, 4]
print(main(arr))