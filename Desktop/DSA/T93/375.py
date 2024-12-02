

#maximum sum

def main(array):

    n=len(array)
    maximum=float("-inf")

    for i in range(n):

        for j in range(i,n):

            subarray=array[i:j+1]

            if len(subarray) >=2:

                new=sorted(subarray)
                one=new[0]
                two=new[1]

                total = one+two

                maximum=max(maximum,total)

    return  maximum

arr = [3, 2, 1]
print(main(arr))