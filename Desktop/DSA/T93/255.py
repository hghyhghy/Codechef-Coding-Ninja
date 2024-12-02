
#kth largest element in the array 


def main(array,k):
    
    array.sort(reverse=True)

    return arr[k-1]

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
K = 2


print(main(arr,K))