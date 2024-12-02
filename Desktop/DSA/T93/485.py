
#longest increasing subsequence

def main(array):

    n=len(array)
    r=[]

    for num in array:

        if not  r or num > r[-1]:

            r.append(num)


        else:

            for i in range(len(r)):

                if r[i] > num :

                    r[i]=num
                    break

    return  len(r)

arr = [3,7,4,6]
print(main(arr))

