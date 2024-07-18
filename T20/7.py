
# The function takes two integrals m and n as arguments. You are required to obtain the total of all integers ranging between 1 to n (both inclusive) which are not divisible by m. You must also return the distinction between the sum of integers not divisible by m with the sum of integers divisible by m.

# Assumption

# m > 0 and n > 0
# Sum lies within the integral range

def sum_of_integers(m,n):

    store1=[]
    store2=[]

    result1=0
    result2=0

    for i in range(1,n+1):

        if i % m == 0:

            store1.append(i)
        
        else :
            
            store2.append(i)

    for num in store1:

        result1 += num

    for num in store2:

        result2 += num

    return result2-result1

m=3
n=10

print(sum_of_integers(m,n))

    