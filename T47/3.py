# Problem statement
# You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

# Note:
# a) Duplicate elements may be present.

# b) If no such element is present return -1.
# Example:
# Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

# Output:  6

def bubble_sort_second_largest(array):
    
    n=len(array)
    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j] < array[j+1]:
                
                array[j],array[j+1]= array[j+1],array[j]

    return array

def main(array):
    
    temporary = bubble_sort_second_largest(array)

    return temporary[1]


a=[2, 4, 5, 6, 8]
print(main(a))