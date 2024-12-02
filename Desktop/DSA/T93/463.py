

#repeating and missing number

def main(array):

    freq={}
    n=len(array)

    for num in array:

        if num in freq:

            freq[num]+=1

        else:

            freq[num]  =1


    repeat=-1
    missing=-1

    for num in range(1,n+1):

        if num in freq:

            if freq[num] ==2:

                repeat = num

        else:

            missing = num

    return  [repeat,missing]

arr = [6, 4, 3, 5, 5, 1]
print(main(arr))
