

# kth largest element

def quick_sort(arr):

    if len(arr) <= 1:

        return arr
    
    else:

        mid= arr[len(arr)//2]
        left=[x for x in arr if x > mid]
        middle=[x for x in arr if x == mid]
        right=[x for x in arr if x < mid]

        return quick_sort(left) + middle + quick_sort(right)


def kth_largest(arr,k):

    temp=quick_sort(arr)

    return temp[k-1]

arr = [3, 2, 1, 5, 6, 4]
k = 2

print(kth_largest(arr,k))