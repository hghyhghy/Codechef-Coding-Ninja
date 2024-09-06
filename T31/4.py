# Problem statement
# You are given a sorted array A consisting of N integers. Your task is to find the magic index in the given array.

# Note :
# 1. A magic index in an array A[0 ... N - 1] is defined to be an index i such that A[i] = i.
# 2. The elements in the array can be negative.
# 3. The elements in the array can be repeated multiple times.
# 4. There can be more than one magic index in an array.

def is_magic_number(arr):
    
    n=len(arr)
    
    if n <=1:
        
        return arr
    
    for i in range(n):
        
        if arr[i] == i:
            
            return arr[i],i
        
    
    return -1

arr = [-10, -5, 1, 3, 7, 9, 12]
print(is_magic_number(arr))

        
    