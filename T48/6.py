# Problem statement
# You are given a non-decreasing array 'arr' consisting of 'n' integers and an integer 'x'. You need to find the first and last position of 'x' in the array.



# Note:
# 1. The array follows 0-based indexing, so you need to return 0-based indices.
# 2. If 'x' is not present in the array, return {-1 -1}.
# 3. If 'x' is only present once in the array, the first and last position of its occurrence will be the same.

def finding_first_and_last_index(array,target):
    
    first =-1
    last=-1
    
    n=len(array)
    
    for i in range(n):
        
        if array[i] ==  target:
            first=i
            break
        
        
    for j in range(n):
        
        if array[j] ==  target:
            last=j

    return first,last

arr = [1, 2, 3, 4, 2, 5, 2, 6]
target = 2
print(finding_first_and_last_index(arr,target))
        