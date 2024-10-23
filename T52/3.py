# Problem statement
# You are given an array consisting of 'N' distinct positive integers and a number 'K'. Your task is to find the kth largest element in the array.

# Example:
# Consider the array {2,1,5,6,3,8} and 'K' = 3, the sorted array will be {8, 6, 5, 3, 2, 1}, and the 3rd largest element will be 5.

def bubble_sort(array):
    
    n=len(array)

    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j] < array[j+1]:
                
                array[j],array[j+1]= array[j+1],array[j]

    return array

def main(array,k):
    
    temp=bubble_sort(array)

    return temp[k-1]

a=[2,1,5,6,3,8]
k=3

print(main(a,k))