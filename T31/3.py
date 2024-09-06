# You are given a sorted array 'arr' of distinct values and a target value 'm'. You need to search for the index of the target value in the array.



# Note:
# 1. If the value is present in the array, return its index.
# 2. If the value is absent, determine the index where it would be inserted in the array while maintaining the sorted order. 
# 3. The given array has distinct integers.
# 4. The given array may be empty.

def finding_the_insert_positions(arr,target):
    
    n=len(arr)

    for index in range(n):
        
        if arr[index] == target:
            
            return index
        
        else:
            
            if target < arr[index]:
                
                return index
            
    return n

arr = [1, 2, 4, 7]
m = 6 

print(finding_the_insert_positions(arr,m))