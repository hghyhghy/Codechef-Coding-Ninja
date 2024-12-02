# Problem statement
# Ninja has been given two sorted integer arrays/lists ‘ARR1’ and ‘ARR2’ of size ‘M’ and ‘N’. Ninja has to merge these sorted arrays/lists into ‘ARR1’ as one sorted array. You may have to assume that ‘ARR1’ has a size equal to ‘M’ + ‘N’ such that ‘ARR1’ has enough space to add all the elements of ‘ARR2’ in ‘ARR1’.

# For example:

# ‘ARR1’ = [3 6 9 0 0]
# ‘ARR2’ = [4 10]
# After merging the ‘ARR1’ and ‘ARR2’ in ‘ARR1’. 
# ‘ARR1’ = [3 4 6 9 10]

def merge_two_sorted_array(arr1:list,arr2:list,m:int,n:int)->list:
    
    i=m-1
    j=n-1
    
    k= m+n-1
    
    while i>=0  and j >=0:
        
        if arr1[i]> arr2[j]:
            
            arr1[k] = arr1[i]
            
            i -=1
            
        else:
            
            arr1[k] =  arr2[j]
            
            j -=1
            
        k -=1
        
    while j >=0:
        
        arr1[k] = arr2[j]
        
        j -= 1
        k -= 1
        
    return arr1
        
ARR1 = [1, 3, 5, 0, 0, 0]  # First list with extra space
ARR2 = [2, 4, 6]  # Second list
m = 3  # Number of valid elements in ARR1
n = 3

print(merge_two_sorted_array(ARR1,ARR2,m,n))