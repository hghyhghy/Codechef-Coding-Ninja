# The function accepts an integer array ‘arr’ of size ‘n’ as its argument. Each element of ‘arr’ represents the number of chocolates distributed to a person. The function needs to return the minimum number of chocolates that need to be distributed to each person so that the difference between the chocolates of any two people is minimized.

def minimum_difference(array,n):
    
    array.sort()

    minimum_difference1=float('inf')

    for start in range(len(array)- n +1):
        
        current_difference= array[start+n-1] - array[start]

        minimum_difference1 = min(minimum_difference1,current_difference)

    return minimum_difference1

arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
n = 3  # Size of subarray
print(minimum_difference(arr,n))