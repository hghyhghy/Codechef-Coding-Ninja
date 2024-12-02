

# difference of indices

def main(array,a,b):

    n=len(array)
    for i in range(n):

        for j in range(i+1,n):

            if abs(array[i]-array[j]) <=b and abs(i-j)<= a:

                return  True

    return  False

ARR = [1, 5, 9, 1, 5, 9]
A = 2
B = 3

print(main(ARR,A,B))