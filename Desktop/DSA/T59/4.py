# Given a sorted array of size N, consisting of only 0’s and 1’s. The problem is to find the position of first ‘1’ in the sorted array Assuming 1 based indexing.

# It could be possible that the array consists of only 0’s or only 1’s. If 1’s are not present in the array then print “-1”

def first_positions(array):
    
    n=len(array)

    for i in range(n):
        
        if array[i]  ==  1:
            
            return i+1

arr1 = [0, 0, 0, 1, 1, 1, 1]
print(first_positions(arr1))