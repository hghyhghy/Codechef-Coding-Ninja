
#selection osrt

def main(array:list[int]):

    n=len(array)

    for  i in range(n):

        minimum=i

        for j in range(i+1,n):

            if array[j]<array[minimum]:

                minimum=j


        array[i],array[minimum]=array[minimum],array[i]

    return  array

number=list(map(int,input().split()))
print(main(number))