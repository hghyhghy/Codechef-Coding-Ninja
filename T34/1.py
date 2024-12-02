# You are given an array of integers. You need to sort the array in ascending order using quick sort.

# Quick sort is a divide and conquer algorithm in which we choose a pivot point and partition the array into two parts i.e, left and right. The left part contains the numbers smaller than the pivot element and the right part contains the numbers larger than the pivot element. Then we recursively sort the left and right parts of the array.

def recursive_quick_sort(array):
    
    if len(array) <= 1:
        
        return array
    
    else:
        
        mid=array[len(array)//2]
        left=[x for x in array if x  < mid]
        middle=[x for x in array if x == mid]
        right=[x for x in array if x > mid]

        return recursive_quick_sort(left) + middle + recursive_quick_sort(right)

array = [ 4, 2, 1, 5, 3 ]
print(recursive_quick_sort(array))