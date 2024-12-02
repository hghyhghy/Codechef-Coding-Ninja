# You are given a sorted array 'arr' of distinct values and a target value 'm'. You need to search for the index of the target value in the array.



# Note:
# 1. If the value is present in the array, return its index.
# 2. If the value is absent, determine the index where it would be inserted in the array while maintaining the sorted order. 
# 3. The given array has distinct integers.
# 4. The given array may be empty.

def find_intersection(array:list,x:int)->int:
    
    n=len(array)
    
    for i in range(n):
        
        if array[i] == x:
            
            return i
        
        elif array[i] > x:
            
            return i
        
    return n

a=[1,2,4,5]
print(find_intersection(a,3))