# Problem statement
# Bubble Sort is one of the sorting algorithms that works by repeatedly swapping the adjacent elements of the array if they are not in sorted order.

# You are given an unsorted array consisting of N non-negative integers. Your task is to sort the array in non-decreasing order using the Bubble Sort algorithm.

def bubble_sorting(array):
    
    n=len(array)

    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j] > array[j+1]:
                
                array[j],array[j+1]=array[j+1],array[j]

    return array

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sorting(arr))

            
            