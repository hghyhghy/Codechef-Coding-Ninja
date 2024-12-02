# You are given an array consisting of 'N' distinct positive integers and a number 'K'. Your task is to find the kth largest element in the array.

# Example:
# Consider the array {2,1,5,6,3,8} and 'K' = 3, the sorted array will be {8, 6, 5, 3, 2, 1}, and the 3rd largest element will be 5.
# Note:
# 1) Kth largest element in an array is the kth element of the array when sorted in non-increasing order. 

# 2) All the elements of the array are pairwise distinct.

def bubble_sort(array:list[int])->list[int]:
    
    n=len(array)
    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j]<array[j+1]:
                
                array[j] ,array[j+1]=array[j+1],array[j]
                
    return array

def kth_largest(array:list[int],k:int)->int:
    
    temp=bubble_sort(array)
    
    return temp[k-1]

arr = [2, 1, 5, 6, 3, 8]
K = 3
print(kth_largest(arr,K))