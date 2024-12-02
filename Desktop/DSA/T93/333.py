

#two sum sorted

def function(array,target):

    n=len(array)

    for i in range(n):

        for j in range(i+1,n):

            if array[i]+array[j]== target:

                return  [i,j]



numbers = [2,7,11,15]
n=9

print(function(numbers,n))