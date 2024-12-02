# Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array. It is given that all array elements are distinct.

# Follow up: Don't solve it using the inbuilt sort function

def bubble_sort(array):
    
    n=len(array)
    
    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j] > array[j+1]:
                
                array[j],array[j+1]=array[j+1],array[j]

    return array

def main(array,k):
    
    tmep=bubble_sort(array)
    
    return tmep[k-1]

arr = [2, 3, 1, 20, 15]
k = 4 
print(main(arr,k))
