

#chocolate

def main(array,m,n):

    if  m ==0 or n == 0:

        return  None

    array.sort()
    minimum=float('inf')

    for i in range(n-m+1):

        difference = array[i+m-1] - array[i]

        minimum=min(minimum,difference)


    return  minimum


N = 5  # Number of packets
M = 3  # Number of students
chocolates = [8, 11, 7, 15, 2]

print(main(chocolates, M, N))
