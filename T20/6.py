

# kth largest elements 

def quicksort(arr):

    if len(arr) <=1 :

        return arr
    
    else:

        mid=  arr[len(arr) // 2]
        left =[x for x in arr if x > mid]
        middle =[ x for x in arr if x == mid ]
        right = [x for x in arr if x<mid]

        return quicksort(left) + middle + quicksort(right)

arr=[5,0,10,6,9,2]
print(quicksort(arr))