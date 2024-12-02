

#subarray range

def main(array,x,y):

    n=len(array)
    count =0

    for i in range(n):

        maximum=array[i]

        for j in range(i,n):

            maximum=max(maximum,array[j])

            if x<=maximum<=y:

                count +=1

    return  count

arr = [1, 2, 3, 4, 5]
X = 2
Y = 4

print(main(arr,X,Y))