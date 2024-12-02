# Problem statement
# You are given three arrays 'A', 'B' and 'C' of length 'N', 'M' and 'K' respectively. All the three arrays are sorted in non-decreasing order. Your task is to find all such elements which are present in all the three given arrays.

# Note:

# 1. The output array should have the same ordering of elements as the original arrays.
# 2. Even if a particular element appears more than once in each of the three arrays, it should still be present only once in the output array.
# 3. If there are no common elements in the arrays, return an empty array.
# For example:

# Consider the three arrays A = [ 2, 3, 4, 7 ] , B = [ 0, 0, 3, 5 ] , C = [ 1, 3, 8, 9 ]
# The output array should be [ 3 ] as 3 is the only element which is present in all the three arrays.

def find_common_elements(array1,array2,array3):
    
    i=j=k=0
    
    common=[]

    while i<len(array1)and j<len(array2) and k<len(array3):
        
        if array1[i] == array2[j] == array3[k]:
            
            common.append(array1[i])

            i += 1
            j += 1
            k += 1
            
        elif array1[i] < array2[j]:
            
            i += 1
            
        elif array2[j] < array3[k]:
            
            j += 1
            
        else:
            
            k += 1
            
            
    return common
arr1 = [1, 5, 10, 20, 40, 80, 100]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(find_common_elements(arr1,arr2,arr3))