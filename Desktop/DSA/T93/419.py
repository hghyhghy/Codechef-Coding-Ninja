

#sum of max and  min

def main(array):

    n=len(array)

    def bubble(array):

        for i in range(n):

            for j in range(0,n-i-1):

                if array[j]>array[j+1]:

                    array[j],array[j+1]=array[j+1],array[j]

        return  array

    temp=bubble(array)

    return  temp[0]+temp[len(temp)-1]

arr = [3, 5, 1, 9, 2]
print(main(arr))