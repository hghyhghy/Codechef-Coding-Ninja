# Problem statement
# Given a rotated sorted array of size ‘N’ and let the elements of the given array be a1,a2,......,an . You need to sort the given array in increasing order.

# For Example - Consider ‘N’ = 4 and the given array is [2,3,4,1] then the output should be [1,2,3,4].

# A rotated sorted array is a sorted array in which each element is shifted ‘x’ (‘x’ >= 0 and ‘x’ <= ’N’) times to its right and the rightmost element is shifted to the beginning of the array.

# For Example - [3,4,1,2] is a rotated sorted array in which each element is shifted two times to its right.

def sort_array_using_bubblesort(array:list[int])->list[int]:
    
    n=len(array)
    
    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j]>array[j+1]:
                
                array[j],array[j+1]=array[j+1],array[j]
                
    return array

a=[6 ,8 ,9 ,2 ,3]
print(sort_array_using_bubblesort(a))